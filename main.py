from lecturas import *
from calculadora import *
from Comparacion import *
def main():
    BetPlay = lecturaBetPlay()
    RushBet = lecturaRushBet()
    Codere = lecturaCodere()
    WPlay = lecturaWPlay()
    print(Codere[0].tipo)
    print(Codere[0].partido)
    print(BetPlay[0].tipo)
    print(BetPlay[0].partido)
    print(RushBet[0].tipo)
    print(RushBet[0].partido)
    print(WPlay[0].tipo)
    print(WPlay[0].partido)
    comparacion('a',True)
if __name__ == '__main__':
    main()
