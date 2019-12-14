from lecturas import *
def main():
    BetPlay = lecturaBetPlay()
    RushBet = lecturaRushBet()
    Codere = lecturaCodere()
    WPlay = lecturaWPlay()
    print(Codere)
    print(Codere[0].tipo)
    print(BetPlay)
    print(BetPlay[0].tipo)
    print(RushBet)
    print(RushBet[0].tipo)
    print(WPlay)
    print(WPlay[0].tipo)
if __name__ == '__main__':
    main()
