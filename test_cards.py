"""
Cards pack tests.    
"""
from ctypes import sizeof
import unittest
from CardsPack import CardsPack

CARDS: str = "KS 2H 5C JD TD"

class TestPokerHandCompareWith(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        
        self.cardsTest = CardsPack(card=CARDS)
        
    def test_PokerHand_shuffle_cards_returns_a_bool(self):
        """Whether shuffle_cards returns a bool"""    
        self.assertIsInstance(self.cardsTest.shuffle_cards(), str)
        
    def test_PokerHand_shuffle_cards_none_cards(self):
        """Whether compare_with is empty"""  
        self.assertIsNotNone(self.cardsTest, "Has no pair to check!")
        
    def test_PokerHand_shuffle_cards_has_5_cards(self):
        """Whether compare_with doesn't have 5 cards"""
        self.assertEqual(len(self.cardsTest), 5, "There are some cards missing!")
    
    
    # handOne = PokerHand(CARDS)    
    # print(len(handOne.hand))
    
    # teste = ['AB', 'AB', 'AB', 'AB']  
    # print(len(teste))
    
if __name__ == "__main__":
    unittest.main()