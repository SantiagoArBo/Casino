from lecturas import partido
def separarDeportes(partidosPorPagina,vectorBase,vectorBase2,vectorBase3):
    m = len(vectorBase)
    partidosPorDeporte = [[[] for j in range(4)] for i in range(m)]
    n = len(partidosPorPagina)
    i = 0
    while i<4:
        for j in partidosPorPagina[i]:
            a = j.tipo.lower()
            w = 0
            entro = False
            while w<m:
                if a == vectorBase[w]:
                    partidosPorDeporte[w][i].append(j)
                    w = m
                    entro = True
                elif a == vectorBase2[w]:
                    partidosPorDeporte[w][i].append(j)
                    w = m
                    entro = True
                elif a == vectorBase3[w]:
                    partidosPorDeporte[w][i].append(j)
                    w = m
                    entro = True
                w=w+1
            if entro is False:
                print("Falta el deporte "+a)
        i = i+1
    return partidosPorDeporte
vectorBase = ["fútbol",\
              "tenis",\
              "baloncesto",\
              "fútbol americano",\
              "hockey sobre hielo",\
              "béisbol",\
              "balonmano",\
              "voleibol",\
              "esquí alpino",\
              "fútbol australiano",\
              "bádminton",\
              "biatlón",\
              "boxeo",\
              "ciclismo",\
              "críquet",\
              "dardos",\
              "esports",\
              "fútbol sala",\
              "fútbol gaélico",\
              "hurling gaélico",\
              "golf",\
              "mma",\
              "carreras de autos",\
              "rugby",\
              "liga de rugby",\
              "waterpolo",\
              "ajedrez",\
              "billar",\
              "deportes de invierno"]
vectorBase2 = ["fútbol",\
              "tenis",\
              "baloncesto",\
              "fútbol americano",\
              "hockey hielo",\
              "béisbol",\
              "balonmano",\
              "voleibol",\
              "esquí alpino",\
              "fútbol australiano",\
              "bádminton",\
              "biatlón",\
              "boxeo",\
              "ciclocross",\
              "críquet",\
              "dardos",\
              "e-sports",\
              "fútbol sala",\
              "fútbol gaélico",\
              "hurling gaélico",\
              "golf",\
              "ufc/mma",\
              "fórmula 1 y motos",\
              "rugby union",\
              "rugby league",\
              "waterpolo",\
              "ajedrez",\
              "billar",\
              "deportes de invierno"]
vectorBase3 = ["fútbol",\
              "tenis",\
              "baloncesto",\
              "fútbol americano",\
              "hockey hielo",\
              "béisbol",\
              "balonmano",\
              "voleibol",\
              "esquí alpino",\
              "fútbol australiano",\
              "bádminton",\
              "biatlón",\
              "boxeo",\
              "ciclismo",\
              "críquet",\
              "dardos",\
              "e-sports",\
              "fútbol sala",\
              "fútbol gaélico",\
              "hurling gaélico",\
              "golf",\
              "artes marciales (ufc/mma)",\
              "carreras de autos",\
              "rugby",\
              "liga de rugby",\
              "waterpolo",\
              "ajedrez",\
              "snooker",\
              "deportes de invierno"]
vectorApuestasBetPlay = [["?","?","Total de goles Más de ","Total de goles Menos ","?","",],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      []]
vectorApuestasCodere = [["Sí","No","Más ","Menos ","","?",],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      []]
vectorApuestasWplay = [["Ambos equipos marcan Sí","Ambos equipos marcan No","Total Más de ","Total Menos de ","Apuesta sin empate","?"],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      [],\
                      []]
