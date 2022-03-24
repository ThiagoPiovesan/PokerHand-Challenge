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
NAIPES: str = "SHDC"
# T = 10, J = Valete, Q = Rainha, K = Rei e A = Ace
CARDS: str = "23456789TJQKA"

class OrganizeCards():

#================================================================================#
    def __init__(self, hand) -> None:
        
        self.hand = hand
#================================================================================#
    def broke_string(self) -> array:
        """Broke the input string into 5 pairs to make the comparation"""
        return self.hand.split(" ")
#================================================================================#
    def getCard_and_Rank(self) -> tuple:
        """Broke the card string into what card is and the rank"""
        self.hand = self.broke_string()
        
        # Find the card value on the string CARDS -> e.g. 2 is 0, 3 is 1, 4 is 2 ...  
        # And how many has in the hand -> e.g. ['9C','9H'] = (8,2) because 9 is 8 (like above) and 2 due to has two 9
        cards_count = {CARDS.find(r): ''.join(self.hand).count(r) for r, _ in self.hand}.items()
        
        # Organize the dict above into 2 tuple -> The first is how many times the card appear 
        # and second is the value of the cards
        # Return in ascendent order and invert it
        cards_score, card_ranks = zip(*sorted((cnt, rank) for rank, cnt in cards_count)[::-1])
        
        print(cards_score)
        print(card_ranks)
        
        # So, we can use a simple pontuation, like these:
        # potential_threeofakind = cards_score[0] == 3
        # potential_twopair = cards_score == (2, 2, 1)
        # potential_pair = cards_score == (2, 1, 1, 1)

        return cards_score, card_ranks
#================================================================================#
    
#================================================================================#
    # def show_cards() -> str:
    #     """Give the cards for the oponnents"""
    #     raise NotImplementedError()
    
if __name__ == "__main__":
    pass