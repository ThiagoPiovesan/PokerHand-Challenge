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
from array import array


class CardsPack():
    def __init__(self, card) -> None:
        
        self.card = card
  
    def shuffle_cards() -> str:
        """shuffle the ranks and cards to give the combination"""
        raise NotImplementedError()
        
    # def show_cards() -> str:
    #     """Give the cards for the oponnents"""
    #     raise NotImplementedError()