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
        positionValue = str(actif["leverage"]*actif["oim"])
        if float(positionValue) > quantite*1.20:
            doublon.append(actif["symbol"].split("_USDT")[0] + "USDT." + str(actif["positionType"]))
    return doublon

futures_client = futures.HTTP("mx0vglt3oXF4bqZzVf", "4032b9bce9ca4095b85fa14db1a479ff")
print(futures_client.assets())