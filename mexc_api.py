from pymexc import futures

api_dic = {
    "bollinger" : {"api_key" : "mx0vglfAsfIbEEwTgv" , "api_secret" : "47b91101f48a443f906b1da50d5abab3"},
    "moving" : {"api_key" : "mx0vglTJinDmmpVhD5" , "api_secret" : "da040ad343294cb98d49dfba5306f179"},
    "x3" : {"api_key" : "mx0vglbsiyENvYy5FA" , "api_secret" : "5be4ae5309d54d61a58354cd653d8dc4"},
    "rsi" : {"api_key" : "mx0vgl8p7abeiGYjJv" , "api_secret" : "e71e698295754d5fbd760f9be1b5da67"},
    "rsi_storj" : {"api_key" : "mx0vglEvS9my97W5Iw", "api_secret" : "6f7bcba8c1ab4685a315a08e0bdc6a1d"}
}
# FUTURES V1

def get_open_position(strategy):
    # initialize HTTP client
    futures_client = futures.HTTP(api_key = api_dic[strategy]["api_key"], api_secret = api_dic[strategy]["api_secret"])
    print(futures_client.open_positions()["data"])
    return len(futures_client.open_positions()["data"])

def get_all_open_position(strategy):
    actif_open = []
    futures_client = futures.HTTP(api_key = api_dic[strategy]["api_key"], api_secret = api_dic[strategy]["api_secret"])
    for actif in futures_client.open_positions()["data"]:
        actif_open.append(actif["symbol"].split("_USDT")[0] + "USDT." + str(actif["positionType"]))
    return actif_open

def checkDoublon(strategy, quantite):
    futures_client = futures.HTTP(api_key = api_dic[strategy]["api_key"], api_secret = api_dic[strategy]["api_secret"])
    doublon = []
    for actif in futures_client.open_positions()["data"]:
        positionValue = str(actif["leverage"]*actif["oim"])
        print(actif["symbol"], positionValue)
        if float(positionValue) > quantite*1.20:
            doublon.append(actif["symbol"].split("_USDT")[0] + "USDT." + str(actif["positionType"]))
    print(doublon)
    return doublon


def get_number_of_open_position(strategy):
    futures_client = futures.HTTP(api_key = api_dic[strategy]["api_key"], api_secret = api_dic[strategy]["api_secret"])
    return len(futures_client.open_positions()["data"])
