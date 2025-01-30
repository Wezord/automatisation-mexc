from pymexc import futures

api_dic = {
    "bollinger" : {"api_key" : "mx0vglfAsfIbEEwTgv" , "api_secret" : "47b91101f48a443f906b1da50d5abab3"},
    "bollinger_ens" : {"api_key" : "mx0vglzDDchtqYfcSv" , "api_secret" : "0989528d21e94419b10bd512d2df3d8a"},
    "bollinger_op" : {"api_key" : "mx0vglWvt05gtwICTa" , "api_secret" : "6abba558a2dc4f02ba7ee853934a3f09"},
    "bollinger_knc" : {"api_key" : "mx0vgll3KI0DzvNQSZ" , "api_secret" : "adbe8010219c41a0a9cbd28077b56813"},
    "moving" : {"api_key" : "mx0vglTJinDmmpVhD5" , "api_secret" : "da040ad343294cb98d49dfba5306f179"},
    "moving_ens" : {"api_key" : "mx0vglwMFY4kgDTuy" , "api_secret" : "918befe9dc584aacb3f6e01742357c19"},
    "moving_xrp" : {"api_key" : "mx0vglpL3yNZmZP9Yb" , "api_secret" : "ccb1aed5c03c433a9ddff58de8dd29fe"},
    "moving_chz" : {"api_key" : "mx0vglpKA29hK3V3fF" , "api_secret" : "66b33720918d4ebaa6fe4933dc46f99e"},
    "x3" : {"api_key" : "mx0vglbsiyENvYy5FA" , "api_secret" : "5be4ae5309d54d61a58354cd653d8dc4"},
    "x3_gala" : {"api_key" : "mx0vglZxPWMR6xpUKj" , "api_secret" : "cf974141445042a882e098fd78ee0bc5"},
    "x3_luna" : {"api_key" : "mx0vgly2jcXHEQ5TXS" , "api_secret" : "3b47dd94df67423291bc94a29807cfb8"},
    "x3_uni" : {"api_key" : "mx0vglbvRw1lFwbRAE" , "api_secret" : "27ca6b3a88c742db937929e74136d9be"},
    "rsi" : {"api_key" : "mx0vgl8p7abeiGYjJv" , "api_secret" : "e71e698295754d5fbd760f9be1b5da67"},
    "rsi_dyd" : {"api_key" : "mx0vglt3oXF4bqZzVf" , "api_secret" : "4032b9bce9ca4095b85fa14db1a479ff"},
    "rsi_atom" : {"api_key" : "mx0vglVKDZ0tAA71zi" , "api_secret" : "2a0e56386f9a47fd99ffa993b2a9edbf"},
    "rsi_storj" : {"api_key" : "mx0vglEvS9my97W5Iw", "api_secret" : "6f7bcba8c1ab4685a315a08e0bdc6a1d"}
}

def get_open_position(strategy):
    # initialize HTTP client
    futures_client = futures.HTTP(api_key = api_dic[strategy]["api_key"], api_secret = api_dic[strategy]["api_secret"])
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
        if float(positionValue) > quantite*1.20:
            doublon.append(actif["symbol"].split("_USDT")[0] + "USDT." + str(actif["positionType"]))
    return doublon


def get_number_of_open_position(strategy):
    futures_client = futures.HTTP(api_key = api_dic[strategy]["api_key"], api_secret = api_dic[strategy]["api_secret"])
    return len(futures_client.open_positions()["data"])
