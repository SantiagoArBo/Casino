import requests
import numpy as np
class partido:
    def __init__(self, tipo, partido, tipo_apuesta, valor):
        self.tipo = tipo
        self.partido = partido
        self.tipo_apuesta = tipo_apuesta
        self.valor = valor
    def darApuesta(self,num):
        respuesta = [self.tipo_apuesta[num], self.valor[num]]
        return respuesta
    def darNumApuestas(self):
        respuesta = len(valor)
        return respuesta
def lecturaBetPlay():
    info = []
    r = requests.get('https://us1-api.aws.kambicdn.com/offering/v2018/bp/event/live/open.json?lang=es_ES&market=CO&client_id=2&channel_id=1&ncid=1575721582313')
    a = r.json()
    for id in a["liveEvents"]:
        tipo = id["event"]["path"][0]["name"]
        r = requests.get('https://us1-api.aws.kambicdn.com/offering/v2018/bp/betoffer/event/'+str(id["event"]["id"])+'.json?lang=es_ES&market=CO&client_id=2&channel_id=1&ncid=1575928857658&includeParticipants=true&type=6')
        data = r.json()
        contador = 0
        str1 = 'a'
        str2 = 'b'
        apuestas = []
        odds = []
        try:
            for i in data["betOffers"]:
                str1 = i["criterion"]["label"]
                for j in i["outcomes"]:
                    str2 = j["label"]
                    odds.append(j["odds"]*0.001)
                    apuestas.append(str1+" "+str2+ " "+str(j["line"]*0.001))
            match = partido(tipo, data["events"][0]["name"], apuestas, odds)
            info.append(match)
        except:
            print("error en algo en el id: "+str(id["event"]["id"])+" en el deporte: "+tipo+", BetPlay")
    return info
def lecturaWPlay():
    dep = list(range(1,21))
    info = []
    for j in dep:
        urlWPlay = 'https://sb1capi-altenar.biahosted.com/Sportsbook/GetLiveEvents?timezoneOffset=300&langId=4&skinName=wplay&configId=1&culture=es&countryCode=CO&deviceType=Desktop&sportids='+str(j)+'&categoryids=0&champids=0&group=Championship&outrightsDisplay=none&couponType=0&filterSingleNodes=2'
        r = requests.get(urlWPlay)
        data = r.json()
        if len(data["Result"]["Items"])>=1:
            for i in data["Result"]["Items"][0]["Items"]:
                for w in i["Events"]:
                    try:
                        deporte = w["SportName"]
                        nombre = w["Name"]
                        apuesta = []
                        valor = []
                        for k in w["Items"]:
                            n = len(k["Items"])
                            if n==2:
                                apuesta.append(k["Name"]+" "+ k["Items"][0]["Name"])
                                apuesta.append(k["Name"]+" "+ k["Items"][1]["Name"])
                                valor.append(k["Items"][0]["Price"])
                                valor.append(k["Items"][1]["Price"])
                        match = partido(deporte, nombre, apuesta, valor)
                        info.append(match)
                    except:
                        print("error en algo en WPlay")
    return info
def lecturaCodere():
    info = []
    r = requests.get('https://m.codere.com.co/csbgonline/home/GetLiveEventsBySportHandle?sporthandle=soccer&languageCode=es-co')
    a = r.json()
    n = len(a)
    i=0
    while i<n:
        for j in a[i]["Events"]:
            apuestas = []
            odds = []
            deporte = j["SportHandle"]
            r = requests.get('https://m.codere.com.co/csbgonline/home/GetGamesLive?parentid='+str(j["NodeId"])+'&languageCode=es-co')
            try:
                data = r.json()
                try:
                    nombre = data["Name"]
                    for k in data["Games"]:
                        if len(k["Results"])==2:
                            for w in k["Results"]:
                                odds.append(w["Odd"])
                                apuestas.append(w["Name"])
                    match = partido(deporte, nombre, apuestas, odds)
                    info.append(match)
                except:
                    print("error en algo en el id: "+str(j["NodeId"])+" en el deporte: "+deporte+", Codere")
            except:
                print("error total en Codere")
        i=i+1
    return info
def lecturaRushBet():
    info = []
    r = requests.get('https://us1-api.aws.kambicdn.com/offering/v2018/rsico/event/live/open.json?lang=es_ES&market=CO&client_id=2&channel_id=1&ncid=1575773160193')
    a = r.json()
    for id in a["liveEvents"]:
        tipo = id["event"]["path"][0]["name"]
        r = requests.get('https://us1-api.aws.kambicdn.com/offering/v2018/rsico/betoffer/event/'+str(id["event"]["id"])+'.json?lang=es_ES&market=CO&client_id=2&channel_id=1&ncid=1575928857658&includeParticipants=true&type=6')
        try:
            data = r.json()
            contador = 0
            str1 = 'a'
            str2 = 'b'
            apuestas = []
            odds = []
            try:
                for i in data["betOffers"]:
                    str1 = i["criterion"]["label"]
                    for j in i["outcomes"]:
                        str2 = j["label"]
                        odds.append(j["odds"]*0.001)
                        apuestas.append(str1+" "+str2+ " "+str(j["line"]*0.001))
                match = partido(tipo, data["events"][0]["name"], apuestas, odds)
                info.append(match)
            except:
                print("error en algo en el id: "+str(id["event"]["id"])+" en el deporte: "+tipo+", RushBet")
        except:
            print("error en algo en el id: "+str(id["event"]["id"])+" en el deporte: "+tipo+", RushBet")
    return info
