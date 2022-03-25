"""
Hand class tests.    
"""
#==================================================================================================#
# Bibliotecas utilizadas:

from ctypes import sizeof
import unittest
from PokerHand import PokerHand

CARDS: str = "KS 2H 5C JD TD"

class TestPokerHandCompareWith(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        
        self.handTest = PokerHand(hand=CARDS)
#=================================================================================#        
    def test_PokerHand_compare_with_returns_a_bool(self):
        """Whether compare_with returns a bool"""    
        self.assertIsInstance(self.handTest.compare_with(), bool)
        
    def test_PokerHand_compare_with_none_cards(self):
        """Whether compare_with is empty"""  
        self.assertIsNotNone(self.handTest.compare_with(), "Has no pair to check!")
        
#=================================================================================#
    def test_PokerHand_evaluate_cards_returns_a_dict(self):
        """Whether evaluate_cards returns a dict"""  
        self.assertIsInstance(self.handTest.evaluate_cards(), None)
    def test_PokerHand_evaluate_cards_none_cards(self):
        """Whether evaluate_cards is empty"""  
        self.assertIsNone(self.handTest.evaluate_cards(), "Has no pair to check!")
#=================================================================================#
    def test_PokerHand_give_score_returns_a_string(self):
        """Whether give_score returns a string"""  
        self.assertIsInstance(self.handTest.give_score(), str)
    def test_PokerHand_give_score_none_cards(self):
        """Whether give_score is empty"""  
        self.assertIsNotNone(self.handTest.give_score(), "Has no pair to check!")
#=================================================================================#

if __name__ == "__main__":
    unittest.main()