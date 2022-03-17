# /*==========================================================*\
# |      /=============================================\       |
# |     ||  - Code develop to shuffle the cards that - ||      |
# |     ||  -      will be used for the players      - ||      |
# |     ||  -         Desafio Python - DATA H        - ||      |
# |     ||  -       Created by: Thiago Piovesan      - ||      |
# |     ||  -          Versao atual: 1.0.0           - ||      |
# |      \=============================================/       |
# \*==========================================================*/

# Link do Github: https://github.com/ThiagoPiovesan

#==================================================================================================#
"""
shuffle and show cards   
"""
#==================================================================================================#
# Bibliotecas utilizadas:
from array import array
import random

#==================================================================================================#
# Important definitions:

# S = Espadas, H = Copas, D = Ouros, C = Paus
NAIPES: str = ["S", "H", "D", "C"]
# T = 10, J = Valete, Q = Rainha, K = Rei e A = Ace
CARDS: str = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

class CardsPack():

#================================================================================#
    def __init__(self) -> None:
        self.Rank = ""
        self.Card = ""
  
    def shuffle_cards(self) -> str:
        """shuffle the ranks and cards to give the combination"""
        raise NotImplementedError()
        
    def remove_cards(self) -> str:
        """Remove cards that has already taken"""
        raise NotImplementedError()
    
    def choose_rank(self) -> str:
        """Choose the card rank => S = Espadas, H = Copas, D = Ouros, C = Paus"""
        self.Rank = NAIPES[random.randint(0, len(NAIPES)-1)]
        return self.Rank
    
    def choose_card(self) -> str:
        """Choose one card from the pack => T = 10, J = Valete, Q = Rainha, K = Rei e A = Ace"""
        self.Card = CARDS[random.randint(0, len(CARDS)-1)]
        return self.Card
#================================================================================#
    # def show_cards() -> str:
    #     """Give the cards for the oponnents"""
    #     raise NotImplementedError()