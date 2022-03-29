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
import sys 

sys.path.append("..")
from EvaluateCards.EvaluateCards import EvaluateCards_and_ScoreGiven

class PokerHand():
    # Win or Loss
    supported_options = {
        'True': 'Win',
        'False': 'Loss'
    }    
    
    
    def __init__(self, hand) -> None:
        
        self.hand = hand
        self.evaluation = EvaluateCards_and_ScoreGiven(self.hand)
        
        self.hand_type, self.pontuation, self.cards_score = self.evaluation.give_score()
        
#==================================================================================================# 
    def compare_with(self, hand2) -> bool:
        """Check between two poker's hand who is the winner"""
    #==================================================================================================#
    # Royal Flush:    
        if self.hand_type == "RoyalFlush":
            self.result = True
            pass
            
        elif hand2.hand_type == "RoyalFlush":
            self.result = False 
            pass
        
    #==================================================================================================#
    # Straight Flush:    
        elif self.hand_type == "StraightFlush":
            self.result = True
            
        elif hand2.hand_type == "StraightFlush":
            self.result = False
            
    #==================================================================================================#
    # Straight Flush:          
        elif self.hand_type == "FoufOfAKind":
            self.result = True
        
    
#==================================================================================================# 

#--------------------------------------------------------------------#       
    # Imprimir itens:
    def __repr__(self, hand2) -> str:
        return f"Hand:('{self.hand}' {PokerHand.supported_options.get(self.result)})"