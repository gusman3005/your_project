class card (object):
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):
        if self.rank in "TJQK":
            return 10
        else:
            return"A23456789".index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return self.rank
    def __str__(self) :
    
        return"%s%s" % (self.rank, self.suit)

class Hand(object):
    def __init__(self, name):
        self.name = name
        self.cards = []
        

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        result = 0
        aces = 0
        for card in self.card:
            result += card.card_value()
            if card.get_rank()=="A":
                aces += 1

        if result + aces * 10<=21:
            result += aces * 10
            return result
    def __str__(self):
        text ="%s's conatains :\n" % self.name
        for card in self.card:
            text +=str(card) + " "
        text += "\nHand value: " + str(self.get_value())
        return text
class Deck(object):
    def __init__(self):
        ranks = "23456789TJQKA"
        suits = "DCHS"
        self.cards = [Card(r,s) for r in ranks for s in suits]
        shuffle(self.cards)
    def deal_card(self):
        return self.card.pop()


def new_game():
    d = deck()
    player_hand = Hand("Player")
    dealer_hand = Hand("Dealer")
    player_hand.add_card(d.deal_card())
    player_hand.add_card(d.deal_card())
    dealer_hand.add_card(d.deal_card())
    print (dealer_hand)
    print ("="*20)
    print (player_hand)
    in_game = true
    while player_hand.get_value() < 21:
        ans = raw_input("Hit or stand? (h/s)")
        if ans == "h":
            print ("You lose")
            in_game = false
        else :
            print ("You stand!")
            break
    print ("="* 20)
    if in_game :
        while dealer_hand.get_value()> 21 :
            dealer_hand.add_card(d.deal_card())
        print (dealer_hand)
        if dealer_hand.get_value()>21:
            print ("Dealer bust")
            in_game = false

        if in_game:
            if player_hand.get_value()> dealer_hand.get_value():
                print ("You win")
            else:
                print ("Dealer win")
