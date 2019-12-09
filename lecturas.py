import requests
import numpy as np
def lecturaBetPlay():
    r = requests.get('https://us1-api.aws.kambicdn.com/offering/v2018/bp/event/live/open.json?lang=es_ES&market=CO&client_id=2&channel_id=1&ncid=1575721582313')
    text = r.text
    n = len(text)
    subinfo = []
    info = []
    i=0
    outcome = False
    odds = False
    participant = False
    actualizar = False
    bandera = False
    inicio = 0
    final = 0
    contador = 0
    while i<n:
        if text[i:i+8]=="outcomes" or outcome:
            outcome = True
            if text[i]=="]":
                bandera = True
                outcome = False
            if text[i]=="}":
                actualizar = True
            if text[i:i+7]=="\"odds\":":
                inicio = i+7
                odds = True
                i=i+7
            if text[i]=="," and odds:
                odds = False
                subinfo.append(text[inicio:i])
            if text[i:i+15]=="\"participant\":\"":
                bandera = False
                inicio = i+15
                participant = True
                i=i+15
            if text[i]=="\"" and participant:
                participant = False
                subinfo.append(text[inicio:i])
        if actualizar:
            actualizar = False
            if len(subinfo)==1:
                try:
                    temp = int(subinfo[0])
                    if bandera:
                        subinfo.append("Desconocido")
                    else:
                        subinfo.append(info[contador-1][1]+"(Empate)")
                except:
                    subinfo=["No odds",subinfo[0]]
            if len(subinfo)==0:
                subinfo.append("No odds")
                subinfo.append("Desconocido")
            info.append(subinfo)
            contador = contador + 1
            subinfo = []
        i=i+1
    return info
def lecturaWPlay():
    # Futbol, baloncesto, hockey, tennis, futbol americano
    dep = ['1','12','16','4','20']
    superInfo = []
    for j in dep:
        urlWPlay = 'https://sb1capi-altenar.biahosted.com/Sportsbook/GetLiveEvents?timezoneOffset=300&langId=4&skinName=wplay&configId=1&culture=es&countryCode=CO&deviceType=Desktop&sportids='+j+'&categoryids=0&champids=0&group=Championship&outrightsDisplay=none&couponType=0&filterSingleNodes=2'
        r = requests.get(urlWPlay)
        text = r.text
        n = len(text)
        subinfo = []
        info = []
        i=0
        inicio = 0
        Name = False
        Price = False
        Items1 = False
        Items2 = False
        Items3 = False
        bandera = False
        actualizar = False
        subinfo = []
        info = []
        while i<n:
            if text[i:i+8]=="\"Items\":" or Items1:
                if (text[i:i+8]=="\"Items\":" or Items2) and Items1:
                    if text[i:i+17]=="\"LiveCurrentTime\"":
                        Items3 = False
                        bandera = False
                        actualizar = True
                        i = i+17
                    if (text[i:i+8]=="\"Items\":" or Items3) and Items2:
                        if text[i:i+8]=="\"Name\":\"":
                            inicio = i+8
                            Name = True
                            i=i+8
                        if text[i:i+8]=="\"Price\":":
                            inicio = i+8
                            Price = True
                            i=i+8
                        if text[i]=="," and Price:
                            subinfo.append(text[inicio:i])
                            Price = False
                        if text[i]=="\"" and Name:
                            if bandera:
                                subinfo.append(text[inicio:i])
                            bandera = True
                            Name = False
                        Items3 = True
                    Items2 = True
                Items1 = True
            if actualizar:
                actualizar = False
                info.append(subinfo)
                subinfo = []
            i=i+1
        superInfo.append(info)
    return superInfo, dep
def lecturaCodere():
    dep = ['soccer','basketball','ice_hockey','tennis','baseball','volleyball','american_football']
    superInfo = []
    for j in dep:
        urlCodere = 'https://m.codere.com.co/csbgonline/home/GetLiveEventsBySportHandle?sporthandle='+j+'&languageCode=es-co'
        r = requests.get(urlCodere)
        text = r.text
        n = len(text)
        subinfo = []
        info = []
        i=0
        Games = False
        Results = False
        Odd = False
        Name = False
        actualizar = False
        subinfo = []
        info = []
        while i<n:
            if text[i:i+8]=="\"Games\":" or Games:
                Games = True
                if text[i]=="]" and not Results:
                    Games = False
                if text[i:i+10]=="\"Results\":":
                    Results = True
                if text[i]=="]":
                    Results = False
                if text[i:i+6]=="\"Odd\":" and Results:
                    inicio = i+6
                    Odd = True
                    i=i+6
                if text[i]=="," and Odd:
                    Odd = False
                    subinfo.append(text[inicio:i])
                if text[i:i+8]=="\"Name\":\"" and Results:
                    inicio = i+8
                    Name = True
                    i=i+8
                if text[i]=="," and Name:
                    Name = False
                    subinfo.append(text[inicio:i-1])
                if text[i]=="}" and Results:
                    actualizar = True
            if actualizar:
                actualizar = False
                if len(subinfo)==1:
                    try:
                        temp = int(subinfo[0])
                        subinfo.append("Desconocido")
                    except:
                        subinfo=["No odds",subinfo[0]]
                if len(subinfo)==0:
                    subinfo.append("No odds")
                    subinfo.append("Desconocido")
                info.append(subinfo)
                subinfo = []
            i=i+1
        superInfo.append(info)
    return superinfo, dep
def lecturaRushBet():
    r = requests.get('https://us1-api.aws.kambicdn.com/offering/v2018/rsico/event/live/open.json?lang=es_ES&market=CO&client_id=2&channel_id=1&ncid=1575773160193')
    text = r.text
    n = len(text)
    subinfo = []
    info = []
    i=0
    outcome = False
    odds = False
    participant = False
    actualizar = False
    bandera = False
    inicio = 0
    final = 0
    contador = 0
    while i<n:
        if text[i:i+8]=="outcomes" or outcome:
            outcome = True
            if text[i]=="]":
                bandera = True
                outcome = False
            if text[i]=="}":
                actualizar = True
            if text[i:i+7]=="\"odds\":":
                inicio = i+7
                odds = True
                i=i+7
            if text[i]=="," and odds:
                odds = False
                subinfo.append(text[inicio:i])
            if text[i:i+15]=="\"participant\":\"":
                bandera = False
                inicio = i+15
                participant = True
                i=i+15
            if text[i]=="\"" and participant:
                participant = False
                subinfo.append(text[inicio:i])
        if actualizar:
            actualizar = False
            if len(subinfo)==1:
                try:
                    temp = int(subinfo[0])
                    if bandera:
                        subinfo.append("Desconocido")
                    else:
                        subinfo.append(info[contador-1][1]+"(Empate)")
                except:
                    subinfo=["No odds",subinfo[0]]
            if len(subinfo)==0:
                subinfo.append("No odds")
                subinfo.append("Desconocido")
            info.append(subinfo)
            contador = contador + 1
            subinfo = []
        i=i+1
    return info
