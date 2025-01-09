import requests

# API endpoint for MEXC Futures server time
url = "https://contract.mexc.com/api/v1/contract/ping"

try:
    # Sending the GET request
    print("request ?")
    response = requests.get(url)
    print("requested")
    response.raise_for_status()  # Raise an error for HTTP errors
    
    # Parse the JSON response
    server_time = response.json()
    print("Server Time:", server_time)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)