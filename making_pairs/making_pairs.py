class MakingPairs(object):
    def __init__(self):
        pass

    def get(self, cards):
        pairs = 0
        for card in cards:
            if card / 2 != 0:
                pairs += card / 2
        return pairs


if __name__ == '__main__':
    cards_complex = [43,23,10,39,39,22,22,0,3,4,3,2]
    cards_single = [5]
    cards_zero = [0]
    cards_ones = [1, 1, 1]
    cards_two = [2, 2, 2]
    m = MakingPairs()
    print m.get(cards_complex)