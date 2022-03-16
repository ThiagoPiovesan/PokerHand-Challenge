"""
Hand class tests.    
"""
from ctypes import sizeof
import unittest
from PokerHand import PokerHand

CARDS: str = "KS 2H 5C JD TD"

class TestPokerHandCompareWith(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        
        self.handTest = PokerHand(hand=CARDS)
        
    def test_PokerHand_compare_with_returns_a_bool(self):
        """Whether compare_with returns a bool"""    
        self.assertIsInstance(self.handTest.compare_with(), bool)
        
    def test_PokerHand_compare_with_none_cards(self):
        """Whether compare_with is empty"""  
        self.assertIsNotNone(self.handTest, "Has no pair to check!")
        
    def test_PokerHand_compare_with_has_5_pairs(self):
        """Whether compare_with doesn't have 5 pairs"""
        self.assertEqual(len(self.handTest), 14, "There are some pairs missing!")
        
        
    def test_PokerHand_broke_string_returns_an_array(self):
        """Whether broke_string is empty"""
        self.assertIsNotNone(self.handTest, "Has no pair to check!")
    
    def test_PokerHand_broke_string_has_5_pairs(self):
        """Whether broke_string doesn't have 5 pairs"""
        self.assertEqual(len(self.handTest), 4, "There are some pairs missing!")
    
    
    # handOne = PokerHand(CARDS)    
    # print(len(handOne.hand))
    
    # teste = ['AB', 'AB', 'AB', 'AB']  
    # print(len(teste))
    
if __name__ == "__main__":
    unittest.main()