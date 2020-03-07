from ListaDeportes import *
class apuesta:
    def __init__(self, especial, localizacion):
        self.especial = partido
        self.localizacion = localizacion
    def darEspecial(self):
        respuesta = self.especial
        return respuesta
    def darLocalizacion(self):
        respuesta = self.localizacion
        return respuesta
def comp(prob1,prob2,prob3,prob4):#prob1 y prob3 son las mismas pero de otras paginas
    valor1 = prob3/(prob1+prob3)
    valor2 = prob4/(prob2+prob4)
    respuesta = [[((valor1*prob1)-1)*100,valor1*100],[((valor2*prob2)-1)*100,valor2*100]]
    return respuesta
def eliminarSolos(partidos):
    nuevos_partidos = []
    for i in partidos:
        actualizar = 0
        for j in i:
            if j == -1:
                actualizar = actualizar + 1
        if actualizar < 3:
            nuevos_partidos.append(i)
    return nuevos_partidos
def evaluar(numeros,partidos,const):
    respuesta = []
    base = [vectorApuestasBetPlay,vectorApuestasBetPlay,vectorApuestasCodere,vectorApuestasWplay]
    for i in numeros:
        guia = [[],[],[],[]]
        j=0
        while j<4:
            b=0
            a = len(base[j][const])
            while b<a:
                guia[j].append([])
                b=b+1
            if i[j] is not -1:
                nombres = partidos[j][i[j]].partido.split(" - ")
                if len(nombres) == 1:
                    nombres = nombres[0].split(" vs ")
                k = 0
                numApuestas = partidos[j][i[j]].darNumApuestas()
                while k<numApuestas:
                    [nombreApuesta, valorApuesta] = partidos[j][i[j]].darApuesta(k)
                    numero = -1
                    for s in nombreApuesta.split():
                        try:
                            numero = float(s)
                        except:
                            pass
                    if numero is not -1:
                        agregado = 0
                        l = 0
                        while l<a and agregado == 0:
                            baseTemp = base[j][const][l]+str(numero)
                            if nombreApuesta == baseTemp:
                                nuevaApuesta = apuesta(numero, k)
                                agregado = 1
                                guia[j][l].append(nuevaApuesta)
                            l = l+1
                        if (agregado == 0) and (j<2):
                            bandera1 = 0
                            bandera2 = 0
                            siguienteNombreApuesta = ""
                            if k<numApuestas-1:
                                [siguienteNombreApuesta, siguienteValorApuesta] = partidos[j][i[j]].darApuesta(k+1)
                            for temp in nombreApuesta.split():
                                if temp == 'Más':
                                    bandera1 = 1
                            for temp in siguienteNombreApuesta.split():
                                if temp == 'Menos':
                                    bandera2 = 1
                            if (bandera1 == 1) and (bandera2 == 1):
                                nuevaApuesta = apuesta(nombreApuesta, k)
                                guia[j][a-1].append(nuevaApuesta)
                    else:
                        l = 0
                        while l<a:
                            for nombrecito in nombres:
                                baseTemp = base[j][const][l]+nombrecito
                                if nombreApuesta == baseTemp:
                                    nuevaApuesta = apuesta(numero, k)
                                    guia[j][l].append(nuevaApuesta)
                            if nombreApuesta == base[j][const][l]:
                                nuevaApuesta = apuesta(numero, k)
                                guia[j][l].append(nuevaApuesta)
                            l = l+1
                    k=k+1
            j=j+1
        iguales(guia)
    return respuesta
def iguales(guia):
    return 0
def Apuestas(numeros,partidos,const):
    nuevos_numeros = eliminarSolos(numeros)
    evaluar(nuevos_numeros,partidos,const)
    return nuevos_numeros
