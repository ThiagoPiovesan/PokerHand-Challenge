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
        True  : 'WIN',
        False : 'LOSS'
    }    
    
    def __init__(self, hand) -> None:
        
        self.hand = hand
        self.evaluation = EvaluateCards_and_ScoreGiven(self.hand)
        
        self.hand_type, self.punctuation, self.cards_score, self.card_ranks = self.evaluation.give_score()
        
#==================================================================================================# 
    def compare_with(self, hand2) -> bool:
        """Check between two poker's hand who is the winner"""
        # Save the second hand to print it later:
        self.hand2 = hand2.hand
        self.hand2_type = hand2.hand_type
        
#==================================================================================================#
    # If the hand One is better then the hand Two:   
        if self.punctuation < hand2.punctuation:
            self.result = True
            return self.result
#==================================================================================================#
    # If the hand One is better then the hand Two:  
        elif self.punctuation > hand2.punctuation:
   
            self.result = False
            return self.result
#==================================================================================================#
    # If the hand One is equal to the hand Two:
    # In this case the higher card wins...    
        else:
            if self.card_ranks[:5][len(self.card_ranks[:5])-1] > hand2.card_ranks[:5][len(self.card_ranks[:5])-1]:
                self.result = True
                return self.result  
            else:
                self.result = False
                return self.result
#==================================================================================================#   
    # Print items:
    def __repr__(self) -> str:
        print("#==================================================================================================#")
        print("# The winner is: \n")
        
        if self.result:
            return f"# The Hand 1:('{self.hand}') -> {PokerHand.supported_options.get(self.result)}, With a ('{self.hand_type}') \n# The Hand 2:('{self.hand2}') -> {PokerHand.supported_options.get(False)}, With a ('{self.hand2_type}')"
        else:
            return f"# The Hand 1:('{self.hand}') -> {PokerHand.supported_options.get(self.result)}, With a ('{self.hand_type}') \n# The Hand 2:('{self.hand2}') -> {PokerHand.supported_options.get(True)}, With a ('{self.hand2_type}')"

#==================================================================================================#      
if __name__ == '__main__':
    # Test:
    hand1 = "TS JS QS KS AS"
    hand2 = "AC AH AS AS KS"

    hand1 = PokerHand(hand1)
    hand2 = PokerHand(hand2)
    
    hand1.compare_with(hand2)
    
    print(hand1)
    
    