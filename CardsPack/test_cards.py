"""
Cards pack tests.    
"""
#==================================================================================================#
# Bibliotecas utilizadas:

from ctypes import sizeof
import unittest
from CardsPack import CardsPack

CARDS: str = "KS 2H 5C JD TD"

class TestCardsPackFunctions(unittest.TestCase):
    """Test if the cards are been choosen correctly and the pack is shuffled """
    
    def setUp(self):
        """Set up test fixtures."""
        
        self.cardsTest = CardsPack()
        
    def test_CardsPack_shuffle_cards_returns_a_bool(self):
        """Whether shuffle_cards returns a string"""    
        self.assertIsInstance(self.cardsTest.shuffle_cards(), str)
        
    def test_CardsPack_shuffle_cards_none_cards(self):
        """Whether shuffle_cards is empty"""  
        self.assertIsNotNone(self.cardsTest.shuffle_cards(), "Has no pair to check!")
        
    def test_CardsPack_shuffle_cards_has_5_cards(self):
        """Whether shuffle_cards doesn't have 5 cards"""
        self.assertEqual(len(self.cardsTest.shuffle_cards()), 5, "There are some cards missing!")
#================================================================================#    
    def test_CardsPack_remove_cards_returns_a_str(self):
        """Whether remove_cards returns a string"""    
        self.assertIsInstance(self.cardsTest.remove_cards(), str)
        
    def test_CardsPack_remove_cards_none_cards(self):
        """Whether remove_cards is empty"""  
        self.assertIsNotNone(self.cardsTest.remove_cards(), "There are no cards!")
#================================================================================#
    def test_CardsPack_choose_rank_returns_a_str(self):
        """Whether choose_rank returns a string"""    
        self.assertIsInstance(self.cardsTest.choose_rank(), str)
        
    def test_CardsPack_choose_rank_none_cards(self):
        """Whether choose_rank is empty"""  
        self.assertIsNotNone(self.cardsTest.choose_rank(), "There are no rank!")
#================================================================================#
    def test_CardsPack_choose_cards_returns_a_str(self):
        """Whether choose_cards returns a string"""    
        self.assertIsInstance(self.cardsTest.choose_card(), str)
        
    def test_CardsPack_choose_cards_none_cards(self):
        """Whether choose_cards is empty"""  
        self.assertIsNotNone(self.cardsTest.choose_card(), "There are no card!")
    
    # handOne = PokerHand(CARDS)    
    # print(len(handOne.hand))
    
    # teste = ['AB', 'AB', 'AB', 'AB']  
    # print(len(teste))
    
if __name__ == "__main__":
    unittest.main()