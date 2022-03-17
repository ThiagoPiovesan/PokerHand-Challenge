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

import argparse
from os import remove
import random
#==================================================================================================#
# S = Espadas, H = Copas, D = Ouros, C = Paus
NAIPES: str = ["S", "H", "D", "C"]
# T = 10, J = Valete, Q = Rainha, K = Rei e A = Ace
CARDS: str = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

#==================================================================================================#
# Main function

if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--hand1', type=str, default='KS 2H 5C JD TD', help="Player's one hand")
#     parser.add_argument('--hand2', type=str, default='9C 9H 5C 5H AC', help="Player's two hand")  # file/folder, 0 for webcam

#     opt = parser.parse_args()
# #==================================================================================================#
#     print('\n#==================================================================================================#')
#     print(opt)
#     print('#==================================================================================================#\n')

    print(CARDS[random.randint(0, len(CARDS)-1)])
    print(NAIPES[random.randint(0, len(NAIPES)-1)])

    table1 = [CARDS[random.randint(0, len(CARDS)-1)] + NAIPES[random.randint(0, len(NAIPES)-1)],
              CARDS[random.randint(0, len(CARDS)-1)] + NAIPES[random.randint(0, len(NAIPES)-1)],
              CARDS[random.randint(0, len(CARDS)-1)] + NAIPES[random.randint(0, len(NAIPES)-1)],
              CARDS[random.randint(0, len(CARDS)-1)] + NAIPES[random.randint(0, len(NAIPES)-1)],
              CARDS[random.randint(0, len(CARDS)-1)] + NAIPES[random.randint(0, len(NAIPES)-1)]]
    
    print(table1)
    
    print(CARDS)
    CARDS.remove(CARDS[random.randint(0, len(CARDS)-1)])
    
    print(CARDS)