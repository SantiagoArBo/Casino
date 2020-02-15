from lecturas import *
from Comparacion import *
from Apuestas import *
from ListaDeportes import *
import time
def main():
    s = time.time()
    BetPlay = lecturaBetPlay()
    RushBet = lecturaRushBet()
    Codere = lecturaCodere()
    WPlay = lecturaWPlay()
    e = time.time()
    v = [len(BetPlay),len(RushBet),len(Codere),len(WPlay)]
    partidosPorPagina = [BetPlay,RushBet,Codere,WPlay]
    partidosPorDeporte = separarDeportes(partidosPorPagina,vectorBase,vectorBase2,vectorBase3)
    res = []
    for i in partidosPorDeporte:
        temp = comparacion(i,False)
        res.append(temp)
    nuevos_res = []
    a = len(partidosPorDeporte)
    i=0
    while i<a:
        # print(vectorBase[i])
        temp = Apuestas(res[i],partidosPorDeporte[i])
        nuevos_res.append(temp)
        #print("-----------------------------------------------------------------")
        i=i+1
    a = len(res)
    b = 0
    contador1 = 0
    contador2 = 0
    while b<a:
        contador1 = contador1 + len(res[b])
        contador2 = contador2 + len(nuevos_res[b])
        for i in res[b]:
            j = 0
            while j<4:
                if i[j] is not -1:
                    try:
                        print(partidosPorDeporte[b][j][i[j]].partido)
                    except:
                        pass
                j=j+1
            print("-------------------------------------------------------------------------------")
        b = b+1
    print(contador1)
    print(contador2)
    print(v)
    print(e-s)
if __name__ == '__main__':
    main()
