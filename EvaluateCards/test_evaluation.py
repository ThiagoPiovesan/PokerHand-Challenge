"""
Hand class tests.    
"""
#==================================================================================================#
# Bibliotecas utilizadas:

import unittest
from EvaluateCards import EvaluateCards_and_ScoreGiven as ec

CARDS: str = "TS JS QS KS AS"

class TestEvaluateCards(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        
        self.handTest = ec(hand=CARDS)

#=================================================================================#
    def test_PokerHand_evaluate_cards_returns_a_string(self):
        """Whether evaluate_cards returns a string"""  
        self.assertIsInstance(self.handTest.evaluate_cards(), str)
        
    def test_PokerHand_evaluate_cards_none_cards(self):
        """Whether evaluate_cards is empty"""  
        self.assertIsNotNone(self.handTest.evaluate_cards(), "Has no pair to check!")
#=================================================================================#
    def test_PokerHand_give_score_returns_a_tuple(self):
        """Whether give_score returns a tuple"""  
        self.assertIsInstance(self.handTest.give_score(), tuple)
        
    def test_PokerHand_give_score_none_cards(self):
        """Whether give_score is empty"""  
        self.assertIsNotNone(self.handTest.give_score(), "Has no pair to check!")
#=================================================================================#

if __name__ == "__main__":
    unittest.main()