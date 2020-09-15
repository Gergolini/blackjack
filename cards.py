import numpy as np
import sys
from utils import value_cards, card_score

np.random.seed(42)

class Cards:
    def __init__(self, n_pack=1, th=30):
        """
        players will be a list of player classes
        :param n_pack: number of packs
        :param th: threshold to reshuffl
        :param current_score: the count score for the current deck
        """
        self.n_pack = n_pack
        self.deck = None
        self.th = th
        self.current_score = 0
    
    def generate_deck(self):
        self.current_score = 0
        cards13 = np.array(list(value_cards.keys()))
        self.deck = np.tile(cards13, self.n_pack)
        np.random.shuffle(self.deck)
    
    def check_cards(self):
        a = self.deck
        if len(a) < self.th:
            e = "Not enough cards to start a new round, reshuffling!"
            print(e)
            self.generate_deck()
        
    def deck_status(self, verbose=False):
        print("{} cards still remaining...".format(len(self.deck)))
        if verbose:
            print(self.deck)
