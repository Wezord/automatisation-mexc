from pymexc import futures

def get_all_open_position(apiKey,secretKey):
    actif_open = []
    futures_client = futures.HTTP(api_key = apiKey, api_secret = secretKey)
    for actif in futures_client.open_positions()["data"]:
        actif_open.append(actif["symbol"].split("_USDT")[0] + "USDT." + str(actif["positionType"]))
    return actif_open

def checkDoublon(quantite,apiKey,secretKey):
    futures_client = futures.HTTP(api_key = apiKey, api_secret = secretKey)
    doublon = []
    for actif in futures_client.open_positions()["data"]:
        positionValue = actif["leverage"]*actif["oim"]
        if positionValue > quantite*1.20:
            doublon.append(actif["symbol"].split("_USDT")[0] + "USDT." + str(actif["positionType"]))
    return doublon

def get_all_open_position(list_api_key, list_secret_key):
    for i in range(len(list_api_key.keys())):
        print(i)