# /*==========================================================*\
# |      /=============================================\       |
# |     ||  -  Code develop to compara two hands at  - ||      |
# |     ||  - poker game and print who is the winner - ||      |
# |     ||  -         Desafio Python - DATA H        - ||      |
# |     ||  -       Created by: Thiago Piovesan      - ||      |
# |     ||  -          Versao atual: 1.0.0           - ||      |
# |      \=============================================/       |
# \*==========================================================*/

# Link do Github: https://github.com/ThiagoPiovesan

#==================================================================================================#
# Bibliotecas utilizadas:

import argparse
from os import remove
import random
#==================================================================================================#
# S = Espadas, H = Copas, D = Ouros, C = Paus
NAIPES: str = ["S", "H", "D", "C"]
# T = 10, J = Valete, Q = Rainha, K = Rei e A = Ace
CARDS: str = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

#==================================================================================================#
# Main function
def calc_score(hand):
    String2: str = "9C 9H 5C 5H AC"
    
    card_ranks_original = '23456789TJQKA'
    original_suits = 'CDHS'
    
    rcounts = {card_ranks_original.find(r): ''.join(hand).count(r) for r, _ in hand}.items()
    score, card_ranks = zip(*sorted((cnt, rank) for rank, cnt in rcounts)[::-1])

    potential_threeofakind = score[0] == 3
    potential_twopair = score == (2, 2, 1, 1, 1)
    potential_pair = score == (2, 1, 1, 1, 1, 1)

    if score[0:2] == (3, 2) or score[0:2] == (3, 3):  # fullhouse (three of a kind and pair, or two three of a kind)
        card_ranks = (card_ranks[0], card_ranks[1])
        score = (3, 2)
    elif score[0:4] == (2, 2, 2, 1):  # special case: convert three pair to two pair
        score = (2, 2, 1)  # as three pair are not worth more than two pair
        sortedCrdRanks = sorted(card_ranks, reverse=True)  # avoid for example 11,8,6,7
        card_ranks = (sortedCrdRanks[0], sortedCrdRanks[1], sortedCrdRanks[2], sortedCrdRanks[3])
    elif score[0] == 4:  # four of a kind
        score = (4,)
        sortedCrdRanks = sorted(card_ranks, reverse=True)  # avoid for example 11,8,9
        card_ranks = (sortedCrdRanks[0], sortedCrdRanks[1])
    elif len(score) >= 5:  # high card, flush, straight and straight flush
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
        suits = [s for _, s in hand]
        flush = max(suits.count(s) for s in suits) >= 5
        if flush:
            for flushSuit in original_suits:  # get the suit of the flush
                if suits.count(flushSuit) >= 5:
                    break

            flushHand = [k for k in hand if flushSuit in k]  # pylint: disable=undefined-loop-variable
            rcountsFlush = {card_ranks_original.find(r): ''.join(flushHand).count(r) for r, _ in flushHand}.items()
            score, card_ranks = zip(*sorted((cnt, rank) for rank, cnt in rcountsFlush)[::-1])
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
        score = ([(1,), (3, 1, 2)], [(3, 1, 3), (5,)])[flush][straight]

    if score == (1,) and potential_threeofakind:
        score = (3, 1)
    elif score == (1,) and potential_twopair:
        score = (2, 2, 1)
    elif score == (1,) and potential_pair:
        score = (2, 1, 1)

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

if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--hand1', type=str, default='KS 2H 5C JD TD', help="Player's one hand")
#     parser.add_argument('--hand2', type=str, default='9C 9H 5C 5H AC', help="Player's two hand")  # file/folder, 0 for webcam

#     opt = parser.parse_args()
# #==================================================================================================#
#     print('\n#==================================================================================================#')
#     print(opt)
#     print('#==================================================================================================#\n')

    # print(CARDS[random.randint(0, len(CARDS)-1)])
    # print(NAIPES[random.randint(0, len(NAIPES)-1)])

    # table1 = [CARDS[random.randint(0, len(CARDS)-1)] + NAIPES[random.randint(0, len(NAIPES)-1)],
    #           CARDS[random.randint(0, len(CARDS)-1)] + NAIPES[random.randint(0, len(NAIPES)-1)],
    #           CARDS[random.randint(0, len(CARDS)-1)] + NAIPES[random.randint(0, len(NAIPES)-1)],
    #           CARDS[random.randint(0, len(CARDS)-1)] + NAIPES[random.randint(0, len(NAIPES)-1)],
    #           CARDS[random.randint(0, len(CARDS)-1)] + NAIPES[random.randint(0, len(NAIPES)-1)]]
    
    # print(table1)
    
    # print(CARDS)
    # CARDS.remove(CARDS[random.randint(0, len(CARDS)-1)])
    
    # print(CARDS)
    hand: str = ["TC", "TH", "5C", "5H", "KH"]
    
    print(calc_score(hand))
    
