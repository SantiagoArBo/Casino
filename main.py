from lecturas import *
from calculadora import *
from Comparacion import *
def main():
    BetPlay = lecturaBetPlay()
    RushBet = lecturaRushBet()
    Codere = lecturaCodere()
    WPlay = lecturaWPlay()
    v = [len(BetPlay),len(RushBet),len(Codere),len(WPlay)]
    partidosPorPagina = [BetPlay,RushBet,Codere,WPlay]
    res = comparacion(partidosPorPagina,False)
    cont = [0,0,0,0]
    for i in res:
        if i[0] is not -1:
            cont[0] = cont[0]+1
        if i[1] is not -1:
            cont[1] = cont[1]+1
        if i[2] is not -1:
            cont[2] = cont[2]+1
        if i[3] is not -1:
            cont[3] = cont[3]+1
    for i in res:
        j = 0
        while j<4:
            if i[j] is not -1:
                print(partidosPorPagina[j][i[j]].partido)
            j=j+1
        print("-------------------------------------------------------------------------------")
    print(cont)
    print(v)
    print(res)
if __name__ == '__main__':
    main()
