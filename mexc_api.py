from pymexc import futures

api_dic = {
    "bollinger" : {"api_key" : "mx0vglfAsfIbEEwTgv" , "api_secret" : "47b91101f48a443f906b1da50d5abab3"}
}
# FUTURES V1

def get_open_position(strategy):
    # initialize HTTP client
    futures_client = futures.HTTP(api_key = api_dic[strategy]["api_key"], api_secret = api_dic[strategy]["api_secret"])
    print(len(futures_client.open_positions()["data"]))
    print(futures_client.open_positions()["data"])
    return len(futures_client.open_positions()["data"])

def get_all_open_position(strategy):
    actif_open = []
    futures_client = futures.HTTP(api_key = api_dic[strategy]["api_key"], api_secret = api_dic[strategy]["api_secret"])
    for actif in futures_client.open_positions()["data"]:
        actif_open.append(actif["symbol"] + str(actif["positionType"]))
    print(actif_open)
    return actif_open

def get_number_of_open_position(strategy):
    futures_client = futures.HTTP(api_key = api_dic[strategy]["api_key"], api_secret = api_dic[strategy]["api_secret"])
    return len(futures_client.open_positions()["data"])

get_all_open_position("bollinger")
