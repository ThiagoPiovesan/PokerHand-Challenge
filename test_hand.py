"""
Hand class testes.    
"""
import unittest
from PokerHand import PokerHand

CARDS: str = "KS 2H 5C JD TD"

class TestPokerHandCompareWith(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        
        self.handOne = PokerHand()