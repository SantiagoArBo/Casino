from lecturas import *
from Comparacion import *
from Apuestas import *
from ListaDeportes import *
import time
def main():
    s = time.time()
    [BetPlay,RushBet,Codere,WPlay] = conexion()
    e = time.time()
    v = [len(BetPlay),len(RushBet),len(Codere),len(WPlay)]
    partidosPorPagina = [BetPlay,RushBet,Codere,WPlay]
    partidosPorDeporte = separarDeportes(partidosPorPagina,vectorBase,vectorBase2,vectorBase3)
    res = []
    # for i in partidosPorDeporte:
    #     temp = comparacion(i,False)
    #     res.append(temp)
    res = comparacion(partidosPorDeporte[0],False)
    nuevos_res = []
    a = len(partidosPorDeporte)
    # i=0
    # while i<a:
    #     temp = Apuestas(res[i],partidosPorDeporte[i],i)
    #     nuevos_res.append(temp)
    #     i=i+1
    nuevos_res = Apuestas(res,partidosPorDeporte[0],0)
    print(v)
    print(e-s)
def conexion():
    try:
        BetPlay = lecturaBetPlay()
    except:
        BetPlay = []
        print("Error conexion BetPlay")
    try:
        RushBet = lecturaRushBet()
    except:
        RushBet = []
        print("Error conexion RushBet")
    try:
        Codere = lecturaCodere()
    except:
        Codere = []
        print("Error conexion Codere")
    try:
        WPlay = lecturaWPlay()
    except:
        WPlay = []
        print("Error conexion WPlay")
    return BetPlay,RushBet,Codere,WPlay
if __name__ == '__main__':
    main()
