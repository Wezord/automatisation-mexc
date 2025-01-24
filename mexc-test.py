import hashlib
import hmac
import urllib.parse
from collections import OrderedDict
import requests
import json
from datetime import datetime


class SignVo:
    def __init__(self, req_time, access_key, secret_key, request_param=""):
        self.req_time = req_time
        self.access_key = access_key
        self.secret_key = secret_key
        self.request_param = request_param


def get_request_param_string(params):
    """
    Generates the query string for GET/DELETE requests.
    :param params: Dictionary of request parameters
    :return: Query string
    """
    if not params:
        return ""
    # Sort parameters alphabetically
    sorted_params = OrderedDict(sorted(params.items()))
    # Build the query string
    param_string = "&".join(
        f"{key}={url_encode(value if value is not None else '')}" for key, value in sorted_params.items()
    )
    return param_string


def url_encode(s):
    """
    Encodes a string using URL encoding.
    :param s: String to encode
    :return: Encoded string
    """
    return urllib.parse.quote(s, safe='').replace('+', '%20')


def actual_signature(input_str, key):
    """
    Generates an HMAC-SHA256 signature.
    :param input_str: Input string to sign
    :param key: Secret key
    :return: Hexadecimal signature string
    """
    return hmac.new(
        key.encode('utf-8'),
        input_str.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()


def sign(sign_vo):
    """
    Generates the signature for the request.
    :param sign_vo: SignVo object containing the details
    :return: Generated signature
    """
    if sign_vo.request_param is None:
        sign_vo.request_param = ""
    # Combine access key, request time, and parameters
    input_str = f"{sign_vo.access_key}{sign_vo.req_time}{sign_vo.request_param}"
    return actual_signature(input_str, sign_vo.secret_key)


def make_get_request(base_url, endpoint, params, access_key, secret_key):
    """
    Makes a GET request with signed parameters.
    :param base_url: API base URL
    :param endpoint: API endpoint
    :param params: Dictionary of request parameters
    :param access_key: API access key
    :param secret_key: API secret key
    :return: API response
    """
    timestamp = str(int(datetime.utcnow().timestamp() * 1000))
    params['timestamp'] = timestamp
    params['api_key'] = access_key

    # Generate query string
    param_string = get_request_param_string(params)

    # Create SignVo and generate signature
    sign_vo = SignVo(req_time=timestamp, access_key=access_key, secret_key=secret_key, request_param=param_string)
    signature = sign(sign_vo)

    # Append signature to query string
    param_string += f"&signature={signature}"

    # Build the final URL
    url = f"{base_url}{endpoint}?{param_string}"

    # Make the GET request
    response = requests.get(url)
    return response.json()

# Example usage: For GET request
if __name__ == "__main__":
    # Example parameters
    BASE_URL = "https://contract.mexc.com/api/v1"
    access_key = "mx0vglfAsfIbEEwTgv"
    secret_key = "47b91101f48a443f906b1da50d5abab3"
    
    # Example GET request
    get_params = {
        "order_id": "123456789"
    }
    get_response = make_get_request(BASE_URL, "/private/order/list/history_orders", get_params, access_key,secret_key)
    print("GET Response:", get_response)
