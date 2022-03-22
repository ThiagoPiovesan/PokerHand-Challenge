"""
Cards pack tests.    
"""
#==================================================================================================#
# Bibliotecas utilizadas:

from ctypes import sizeof
import unittest
from OrganizeCards import OrganizeCards

CARDS: str = "KS 2H 5C JD TD"

class TestOrganizeCardsFunctions(unittest.TestCase):
    """Test if the cards are been choosen correctly and the pack is shuffled """
    
    def setUp(self):
        """Set up test fixtures."""
        
        self.cardsTest = OrganizeCards(CARDS)

    #=================================================================================#        
    def test_OrganizeCards_broke_string_returns_an_array(self):
        """Whether broke_string is empty"""
        self.assertIsNotNone(self.cardsTest.broke_string(), "Has no pair to check!")
    
    def test_OrganizeCards_broke_string_has_5_pairs(self):
        """Whether broke_string doesn't have 5 pairs"""
        self.assertEqual(len(self.cardsTest.broke_string()), 5, "There are some pairs missing!")
#=================================================================================#        
    def test_OrganizeCards_getCard_and_Rank_returns_an_str(self):
        """Whether broke_string is empty"""
        self.assertIsNotNone(self.cardsTest.getCard_and_Rank(), "Has no pair to check!")
    
    def test_OrganizeCards_getCard_and_Rank_has_2_itens(self):
        """Whether broke_string doesn't have 5 pairs"""
        self.assertEqual(len(self.cardsTest.getCard_and_Rank()), 2, "There are some pairs missing!")


    
    # teste = ['AB', 'AB', 'AB', 'AB']  
    # print(len(teste))
    
if __name__ == "__main__":
    unittest.main()