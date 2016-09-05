
class Plusonegame():

    def getorder(self, s):
        number_plus = []
        cards = []
        result = ''
        for char in s:
            if char != '+':
                cards.append(int(char))
            else:
                number_plus.append('+')
        sorted(cards)
        if len(cards) > 0:
            for card in cards:
                if card == 0:
                    result += str(card)
                else:
                    if len(number_plus) > 0:
                        if card <= len(number_plus):
                            result += ''.join(number_plus[:card])+card
                            number_plus = [card:]
                        else:
                            pass
                    else:
                        result += str(card)
        return result

if __name__ == '__main__':
    s = "1++"
    game = Plusonegame()
    print game.getorder(s)