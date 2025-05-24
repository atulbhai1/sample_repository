class Card:
    def __init__(self, card):
        self.card = card
        self.color = card[0]
        self.number = card[1]
        self.symbol = card[2]
        self.card_list = [self.color, self.number, self.symbol]

    def __eq__(self, other):
        if type(other) == Card:
            counter_of_similarities = 0
            for list_spot, part in enumerate(self.card_list):
                if part == other.card_list[list_spot]:
                    counter_of_similarities += 1

            if counter_of_similarities == 2:
                return True
            else:
                return False
        else:
            raise ValueError(
                "Need to perform equality btw Cards and Cards. Cards cannot be compared to other type objects.")

    def __str__(self):
        return self.card


def printPile(piles, hand):
    piles = piles.split()
    piles_copy = piles.copy()
    piles = []
    hand = hand.split()
    hand_copy = hand.copy()
    hand = []
    for pile in piles_copy:
        piles.append(Card(pile))

    for han in hand_copy:
        hand.append(Card(han))
    hand_copy = hand.copy()
    made_piles = []

    for pile_card in piles:
        hand = hand_copy.copy()
        possible = True
        pile = [pile_card]
        while possible:
            possible = False
            for place, card in enumerate(hand):
                if card == pile[-1]:
                    pile.append(card)
                    hand.pop(place)
                    possible = True
                    break
        made_piles.append(pile)

    longest_pile = []

    for pile in made_piles:
        if len(pile) > len(longest_pile):
            longest_pile = pile

    pile_text = " ".join(str(i) for i in longest_pile)

    return pile_text

print(printPile("G2T G3X", "Y1S G4S B4S G2S R1T G2X Y2T"))