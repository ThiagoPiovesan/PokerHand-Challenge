# /*==========================================================*\
# |      /=============================================\       |
# |     ||  -  Code develop to compare two hands at  - ||      |
# |     ||  - poker game and print who is the winner - ||      |
# |     ||  -         Desafio Python - DATA H        - ||      |
# |     ||  -       Created by: Thiago Piovesan      - ||      |
# |     ||  -          Versao atual: 1.0.0           - ||      |
# |      \=============================================/       |
# \*==========================================================*/

# Link do Github: https://github.com/ThiagoPiovesan

#==================================================================================================#
"""
Poker hand compare system.    
"""
#==================================================================================================#
# Bibliotecas utilizadas:

from array import array


class PokerHand():

    def __init__(self, hand) -> None:
        
        self.hand = hand
  
    def compare_with() -> bool:
        """Check between two poker's hand who is the winner"""
        raise NotImplementedError()

    def broke_string() -> array:
        """Broke the input string into 5 pairs to make the comparation"""
        raise NotImplementedError()