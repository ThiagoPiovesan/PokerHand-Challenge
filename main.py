# /*==========================================================*\
# |      /=============================================\       |
# |     ||  -  Code develop to compara two hands at  - ||      |
# |     ||  - poker game and print who is the winner - ||      |
# |     ||  -         Desafio Python - DATA H        - ||      |
# |     ||  -       Created by: Thiago Piovesan      - ||      |
# |     ||  -          Versao atual: 1.0.0           - ||      |
# |      \=============================================/       |
# \*==========================================================*/

# Link do Github: https://github.com/ThiagoPiovesan

#==================================================================================================#
# Bibliotecas utilizadas:
from PokerHand import PokerHand as PH

#==================================================================================================#
# S = Espadas, H = Copas, D = Ouros, C = Paus
NAIPES: str = ["S", "H", "D", "C"]
# T = 10, J = Valete, Q = Rainha, K = Rei e A = Ace
CARDS: str = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

#==================================================================================================#

if __name__ == '__main__':
    # Test:
    hand1 = "TS JS QS KS AS"
    hand2 = "AC AH AS AS KS"

    hand1 = PH.PokerHand(hand1)
    hand2 = PH.PokerHand(hand2)
    
    hand1.compare_with(hand2)
    
    print(hand1)
    