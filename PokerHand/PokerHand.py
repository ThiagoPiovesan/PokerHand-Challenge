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

class PokerHand():
    # S = Espadas, H = Copas, D = Ouros, C = Paus
    NAIPES: str = "SHDC"
    # T = 10, J = Valete, Q = Rainha, K = Rei e A = Ace
    CARDS: str = "23456789TJQKA"

    def __init__(self, hand) -> None:
        
        self.hand = hand
        self.organizer = OrganizeCards(self.hand)
  
    def compare_with(self, hand1, hand2) -> bool:
        """Check between two poker's hand who is the winner"""
        raise NotImplementedError()

    def evaluate_cards(self) -> dict:
        """Evaluate the hand and give the pontuation expect for those cards

        Returns:
            dict: Combination of possible combos...
        """
        cards_score, card_ranks = self.organizer.getCard_and_Rank()
        
        if cards_score[0:2] == (3, 2) or cards_score[0:2] == (3, 3):  # fullhouse (three of a kind and pair, or two three of a kind)
            card_ranks = (card_ranks[0], card_ranks[1])
            cards_score = (3, 2)
            
        elif cards_score[0:4] == (2, 2, 2, 1):  # special case: convert three pair to two pair
            cards_score = (2, 2, 1)  # as three pair are not worth more than two pair
            sortedCrdRanks = sorted(card_ranks, reverse=True)  # avoid for example 11,8,6,7
            card_ranks = (sortedCrdRanks[0], sortedCrdRanks[1], sortedCrdRanks[2], sortedCrdRanks[3])
            
        elif cards_score[0] == 4:  # four of a kind
            cards_score = (4,)
            sortedCrdRanks = sorted(card_ranks, reverse=True)  # avoid for example 11,8,9
            card_ranks = (sortedCrdRanks[0], sortedCrdRanks[1])
            
        elif len(cards_score) >= 5:  # high card, flush, straight and straight flush
            # straight
            if 12 in card_ranks:  # adjust if 5 high straight
                card_ranks += (-1,)
            sortedCrdRanks = sorted(card_ranks, reverse=True)  # sort again as if pairs the first rank matches the pair
            for i in range(len(sortedCrdRanks) - 4):
                straight = sortedCrdRanks[i] - sortedCrdRanks[i + 4] == 4
                if straight:
                    card_ranks = (
                        sortedCrdRanks[i], sortedCrdRanks[i + 1], sortedCrdRanks[i + 2], sortedCrdRanks[i + 3],
                        sortedCrdRanks[i + 4])
                    break

            # flush
            suits = [s for _, s in self.hand]
            flush = max(suits.count(s) for s in suits) >= 5
            if flush:
                for flushSuit in self.NAIPES:  # get the suit of the flush
                    if suits.count(flushSuit) >= 5:
                        break

                flushHand = [k for k in self.hand if flushSuit in k]  # pylint: disable=undefined-loop-variable
                rcountsFlush = {self.CARDS.find(r): ''.join(flushHand).count(r) for r, _ in flushHand}.items()
                cards_score, card_ranks = zip(*sorted((cnt, rank) for rank, cnt in rcountsFlush)[::-1])
                card_ranks = tuple(
                    sorted(card_ranks, reverse=True))  # ignore original sorting where pairs had influence

                # check for straight in flush
                if 12 in card_ranks and -1 not in card_ranks:  # adjust if 5 high straight
                    card_ranks += (-1,)
                for i in range(len(card_ranks) - 4):
                    straight = card_ranks[i] - card_ranks[i + 4] == 4
                    if straight:
                        break

            # no pair, straight, flush, or straight flush
            cards_score = ([(1,), (3, 1, 2)], [(3, 1, 3), (5,)])[flush][straight]
            
        if cards_score[0] == 5:
            hand_type = "StraightFlush"
            # crdRanks=crdRanks[:5] # five card rule makes no difference {:5] would be incorrect
        elif cards_score[0] == 4:
            hand_type = "FoufOfAKind"
            # crdRanks=crdRanks[:2] # already implemented above
        elif cards_score[0:2] == (3, 2):
            hand_type = "FullHouse"
            # crdRanks=crdRanks[:2] # already implmeneted above
        elif cards_score[0:3] == (3, 1, 3):
            hand_type = "Flush"
            card_ranks = card_ranks[:5]
        elif cards_score[0:3] == (3, 1, 2):
            hand_type = "Straight"
            card_ranks = card_ranks[:5]
        elif cards_score[0] == 3:
            hand_type = "ThreeOfAKind"
            card_ranks = card_ranks[:3]
        elif cards_score[0:2] == (2, 2):
            hand_type = "TwoPair"
            card_ranks = card_ranks[:3]
        elif cards_score[0] == 2:
            hand_type = "Pair"
            card_ranks = card_ranks[:4]
        elif cards_score[0] == 1:
            hand_type = "HighCard"
            card_ranks = card_ranks[:5]
        else:
            raise Exception('Card Type error!')

        return cards_score, card_ranks, hand_type    

    def give_score(self):
        """
            Give the cards score recieved from the evaluation made before.
        """
        
        if score[0] == 5:
            hand_type = "StraightFlush"
            # crdRanks=crdRanks[:5] # five card rule makes no difference {:5] would be incorrect
        elif score[0] == 4:
            hand_type = "FoufOfAKind"
            # crdRanks=crdRanks[:2] # already implemented above
        elif score[0:2] == (3, 2):
            hand_type = "FullHouse"
            # crdRanks=crdRanks[:2] # already implmeneted above
        elif score[0:3] == (3, 1, 3):
            hand_type = "Flush"
            card_ranks = card_ranks[:5]
        elif score[0:3] == (3, 1, 2):
            hand_type = "Straight"
            card_ranks = card_ranks[:5]
        elif score[0] == 3:
            hand_type = "ThreeOfAKind"
            card_ranks = card_ranks[:3]
        elif score[0:2] == (2, 2):
            hand_type = "TwoPair"
            card_ranks = card_ranks[:3]
        elif score[0] == 2:
            hand_type = "Pair"
            card_ranks = card_ranks[:4]
        elif score[0] == 1:
            hand_type = "HighCard"
            card_ranks = card_ranks[:5]
        else:
            raise Exception('Card Type error!')

        return score, card_ranks, hand_type
    
    
if __name__ == "__main__":
    hand2: str = "9C 9H 5C 5H AC"
        
    poker = PokerHand(hand2)

    print(poker.evaluate_cards())