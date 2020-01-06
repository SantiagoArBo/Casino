from lecturas import partido
def prepros(partidosPorPaginas,debug):
    respuesta = []
    for pagina in partidosPorPaginas:
        respuesta1 = []
        for partidos in pagina:
            n = partidos.lower()
            n = n.replace('team','')
            n = n.replace('club','')
            n1 = n.split("-")
            if len(n1) == 1:
                n1 = n.split("vs.")
            i = 0
            while i<len(n1):
                a = n1[i].split(" ")
                for j in a:
                    if len(j)<4:
                        n1[i] = n1[i].replace(j,'')
                n1[i] = n1[i].replace('  ',' ')
                n1[i] = n1[i].strip()
                i = i+1
            respuesta1.append(n1)
        respuesta.append(respuesta1)
    return respuesta
def ordenar(partidosPorPaginas,debug):
    respuesta = []
    m = []
    for i in partidosPorPaginas:
        m.append(len(i))
    val = m.index(max(m))
    i = 0
    while i<m[val]:
        number = [-1,-1,-1,-1]
        number[val] = i
        j = 0
        while j<4:
            if j is not val:
                w = 0
                while w<m[j]:
                    a = comparar(partidosPorPaginas[val][i],partidosPorPaginas[j][w])
                    if a > 0.8:
                        number[j] = w
                        w = 9999999999
                    w = w+1
            j = j+1
        respuesta.append(number)
        i = i+1
    return respuesta
def comparar(a1,a2):
    n1 = len(a1)
    n2 = len(a2)
    res = 0
    if n1==n2:
        i=0
        while i<n1:
            j=0
            maximo = 0
            s1 = max(a1[i].split(" "),key=len)
            while j<n1 and i<n1:
                if sorted(a1[i])==sorted(a2[j]):
                    res = res + 0.5
                    i=i+1
                else:
                    s2 = max(a2[j].split(" "),key=len)
                    m = max(len(s1),len(s2))
                    mi = min(len(s1),len(s2))
                    temp = 0
                    k = 0
                    while k<mi:
                        if s1[k]==s2[k]:
                            temp = temp + (0.5/m)
                        k=k+1
                    if temp > maximo:
                        maximo = temp
                    j = j+1
            res = res + maximo
            i=i+1
    return res
def comparacion(partidosPorPaginas,debug):
    if debug:
        partidosPorPaginas = [["Real Mádrid - Barcelona FC", "chalke 04 - BaYeR del Munchen", "Olympia Real - Millonarios TEAM", "America s54 - Real Popayan"],\
                  ["Olympia - Millonarios", "America - Popayan Real","Real Madrid - FC Barcelona", "Chalke 04 - BaieR del Munchen"],\
                  ["BaYeR del Munchen - chalke 04","Barcelona FC - Real Mádrid","Real Popayan - America s54","Millonarios TEAM - Olympia Real",],\
                  ["Real Popayan vs. America s54","Olympia Real vs. Millonarios","chalke 04 vs. Munchen"]]
    nombres = prepros(partidosPorPaginas,debug)
    print(nombres)
    respuesta = ordenar(nombres,debug)
    print(respuesta)