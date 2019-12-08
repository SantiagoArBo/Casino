import requests
import numpy as np
def lecturaBetPlay(urlBetPlay):
    r = requests.get(urlBetPlay)
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
def lecturaWPlay(urlWPlay):
    return info
def lecturaCodere():
    const = ['soccer','american_football','basketball']
    for j in const:
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
    return info
def lecturaRushBet(urlRushBet):
    r = requests.get(urlRushBet)
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
