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
from CardsControl.OrganizeCards import OrganizeCards


class EvaluateCards_and_ScoreGiven():
    # S = Espadas, H = Copas, D = Ouros, C = Paus
    NAIPES: str = "SHDC"
    # T = 10, J = Valete, Q = Rainha, K = Rei e A = Ace
    CARDS: str = "23456789TJQKA"
    
    def __init__(self, hand) -> None:
        
        self.hand = hand
        self.organizer = OrganizeCards(self.hand)
        
        self.cards_score, self.card_ranks, self.hand = self.organizer.getCard_and_Rank()
        
        self.royal = False      # Constant False but when we have a Royal Flush
#==================================================================================================#
    def give_score(self) -> tuple:
        """
            Give the cards score received from the evaluation made before.
        """
        print(self.evaluate_cards())
        
        if self.cards_score[0] == 5 and self.royal:
            hand_type = "RoyalFlush"
            punctuation = 0
        elif self.cards_score[0] == 5:
            hand_type = "StraightFlush"
            punctuation = 1
        elif self.cards_score[0] == 4:
            hand_type = "FoufOfAKind"
            punctuation = 2
        elif self.cards_score[0:2] == (3, 2):
            hand_type = "FullHouse"
            punctuation = 3
        elif self.cards_score[0:3] == (3, 1, 3):
            hand_type = "Flush"
            self.card_ranks = self.card_ranks[:5]
            punctuation = 4
        elif self.cards_score[0:3] == (3, 1, 2):
            hand_type = "Straight"
            self.card_ranks = self.card_ranks[:5]
            punctuation = 5
        elif self.cards_score[0] == 3:
            hand_type = "ThreeOfAKind"
            self.card_ranks = self.card_ranks[:3]
            punctuation = 6
        elif self.cards_score[0:2] == (2, 2):
            hand_type = "TwoPair"
            self.card_ranks = self.card_ranks[:3]
            punctuation = 7
        elif self.cards_score[0] == 2:
            hand_type = "Pair"
            self.card_ranks = self.card_ranks[:4]
            punctuation = 8
        elif self.cards_score[0] == 1:
            hand_type = "HighCard"
            self.card_ranks = self.card_ranks[:5]
            punctuation = 9
        else:
            raise Exception('Card Type error!')
        
        return hand_type, punctuation, self.cards_score, self.card_ranks
#==================================================================================================# 
    def evaluate_cards(self):
        """Evaluate the hand and give the punctuation expect for those cards

        """
    #==================================================================================================#    
        if self.cards_score[0:2] == (3, 2) or self.cards_score[0:2] == (3, 3):  # fullhouse 
                                                                                #(three of a kind and pair, or two three of a kind)
            self.card_ranks = (self.card_ranks[0], self.card_ranks[1])
            self.cards_score = (3, 2)
    #==================================================================================================#        
        elif self.cards_score[0:4] == (2, 2, 2, 1):                             # special case: convert three pair to two pair
            self.cards_score = (2, 2, 1)                                        # as three pair are not worth more than two pair
            sortedCrdRanks = sorted(self.card_ranks, reverse=True)  
            self.card_ranks = (sortedCrdRanks[0], sortedCrdRanks[1], sortedCrdRanks[2], sortedCrdRanks[3])
    #==================================================================================================#        
        elif self.cards_score[0] == 4:                                          # four of a kind
            self.cards_score = (4,)
            sortedCrdRanks = sorted(self.card_ranks, reverse=True)              # avoid for example 11,8,9
            self.card_ranks = (sortedCrdRanks[0], sortedCrdRanks[1])
    #==================================================================================================#        
        elif len(self.cards_score) >= 5:                                        # high card, flush, straight and straight flush
            # Straight ...
            
            if 12 in self.card_ranks:                                           # adjust if 5 high straight
                self.card_ranks += (-1,)
                
            sortedCrdRanks = sorted(self.card_ranks, reverse=True)              # sort again as if pairs the first rank matches the pair
           
            for i in range(len(sortedCrdRanks) - 4):
                straight = sortedCrdRanks[i] - sortedCrdRanks[i + 4] == 4
                
                if straight:
                    self.card_ranks = (
                        sortedCrdRanks[i], sortedCrdRanks[i + 1], sortedCrdRanks[i + 2], sortedCrdRanks[i + 3],
                        sortedCrdRanks[i + 4])
                    break
        #==================================================================================================#            
            # Flush...
            suits = [s for _, s in self.hand]

            flush = max(suits.count(s) for s in suits) >= 5
            if flush:
                
                for flushSuit in self.NAIPES:                                   # Get the suit of the flush
                    
                    if suits.count(flushSuit) >= 5:
                        break

                flushHand = [k for k in self.hand if flushSuit in k]    
                rcountsFlush = {self.CARDS.find(r): ''.join(flushHand).count(r) for r, _ in flushHand}.items()
                
                self.cards_score, self.card_ranks = zip(*sorted((cnt, rank) for rank, cnt in rcountsFlush)[::-1])
                self.card_ranks = tuple(
                    sorted(self.card_ranks, reverse=True))                      # Ignore original sorting where pairs had influence

                # check for straight in flush
                if 12 in self.card_ranks and -1 not in self.card_ranks:         # Adjust if 5 high straight
                    self.card_ranks += (-1,)
                    
                for i in range(len(self.card_ranks) - 4):
                
                    straight = self.card_ranks[i] - self.card_ranks[i + 4] == 4
                    
                    if straight and self.card_ranks[i] == 12:
                        self.royal = True
                        break
                    else:
                        break
        #==================================================================================================#
            # no pair, straight, flush, or straight flush
            self.cards_score = ([(1,), (3, 1, 2)], [(3, 1, 3), (5,)])[flush][straight]
        #==================================================================================================#    
        return "Cards Score: {}".format(self.cards_score) 
#==================================================================================================#
