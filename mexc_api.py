from pymexc import futures

def get_all_open_position(apiKey,secretKey):
    actif_open = []
    futures_client = futures.HTTP(api_key = apiKey, api_secret = secretKey)
    if futures_client == None:
        return "Error dans la connection à l'API"
    results = futures_client.open_positions()
    if "data" not in results or not results["data"]:
        return actif_open
    else:
        for actif in futures_client.open_positions()["data"]:
            actif_open.append(actif["symbol"].split("_USDT")[0] + "USDT." + str(actif["positionType"]))
        return actif_open

def checkDoublon(quantite,apiKey,secretKey):
    futures_client = futures.HTTP(api_key = apiKey, api_secret = secretKey)
    doublon = []
    if futures_client == None:
        return "Error dans la connection à l'API"
    for actif in futures_client.open_positions()["data"]:
        positionValue = actif["leverage"]*actif["oim"]
        if positionValue > quantite*1.20:
            doublon.append(actif["symbol"].split("_USDT")[0] + "USDT." + str(actif["positionType"]))
    return doublon