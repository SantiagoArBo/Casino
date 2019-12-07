import requests
import numpy as np
url='https://us1-api.aws.kambicdn.com/offering/v2018/bp/event/live/open.json?lang=es_ES&market=CO&client_id=2&channel_id=1&ncid=1575721582313'
r = requests.get(url)
text = r.text
print(text.encode('utf-8'))
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
print(len(info))
contador = 1
for i in info:
    print(i[0],i[1].encode('utf-8'),contador)
    contador = contador+1
