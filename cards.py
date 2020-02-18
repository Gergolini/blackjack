import numpy as np

np.random.seed(42)

value_cards={'A':[1,11],
    "K":10,
    "Q":10,
    "J":10}

num_values = {str(i):i for i in range(2,11)}
value_cards.update(num_values)
#print(value_cards)

class Cards:
    def __init__(self, n_pack=1, th=30):
        """
        players will be a list of player classes
        """
        self.n_pack = n_pack
        self.deck = None
        self.th = th
    
    def generate_deck(self):
        cards13 = np.array(list(value_cards.keys()))
        self.deck = np.tile(cards13, 4*self.n_pack)
        np.random.shuffle(self.deck)
    
    def check_cards(self):
        a = self.deck
        if len(a) < 2:
            e = "Not enough cards to start a new round, reshuffling!"
            print(e)
            self.generate_deck()
        
    def print_deck(self):
        print(self.deck)

#card=Cards(2)
#card.generate_deck()
#card.check_cards()
#card.print_deck()
    
#card = Cards(players=5)
#card.generate_deck()
#
#card.print_deck()
#card.deal_deck()

"""
1. combine generate and shuffle to generate
2. write a function deal 2 cards to players (take a list of players as arguments)
3. write a function to check the number of cards left, and print error msg when not enough cards.
4. Write a prototype of a player class, think about what attributes they should have
"""
