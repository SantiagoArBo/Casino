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
def evaluar(numeros,partidos):
    respuesta = []
    # v = ["BetPlay","RushBet","Codere","WPlay"]
    # for i in numeros:
    #     j=0
    #     while j<4:
    #         print(v[j])
    #         if i[j] is not -1:
    #             try:
    #                 print(partidos[j][i[j]].partido)
    #                 print(partidos[j][i[j]].tipo_apuesta)
    #             except:
    #                 pass
    #         j=j+1
    #     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    return respuesta
def Apuestas(numeros,partidos):
    nuevos_numeros = eliminarSolos(numeros)
    evaluar(nuevos_numeros,partidos)
    return nuevos_numeros
