import numpy as np

from utils import value_cards, card_score

# np.random.seed(42)

class Dealer:
    def __init__(self):
        self.cards = np.array([])
        self.stop = False
        self.stop_num = 17
        self.name = 'Dealer'
        self.total_points = 0
        self.isbj = False
        self.bust = False

    def take_cards(self, ob_cards, num_cards=1, init=False):
        top = ob_cards.deck[:num_cards]
        for c in top:
            ob_cards.current_score += card_score[c]
        ob_cards.deck = ob_cards.deck[num_cards:]
        self.cards = np.concatenate([self.cards, top])
        print(self.name, init)
        if init:
            print("player {} taking 2 starting cards ...".format(self.name))
        else:
            print("player {} taking 1 card ...".format(self.name))
        print(self.cards, self.calc_points())
        print("Current card score: {}".format(ob_cards.current_score))
        
    def init_cards(self, ob_cards):
        self.isbj = False
        self.stop = False
        self.take_cards(ob_cards, 2, init=True)
        if self.calc_points() == 21:
            self.isbj = True
            self.stop = True
            self.total_points = 21
    
    def clear_cards(self):
        self.cards = np.array([])
    
    def calc_points(self):
        res = 0
        n_Ace = self.cards.tolist().count('A')
        for card in self.cards:
            if card != 'A':
                res += value_cards[card]
            else:
                res += 11
        while n_Ace > 0 and res > 21:
            res -= 10
            n_Ace -= 1
        return res
    
    def print_cards(self):
        print(self.cards)
        
    def stop_by(self, ob_cards):
        self.bust = False
        while not self.stop:
            self.total_points = self.calc_points()
            p = self.total_points
            if p < self.stop_num:
                self.take_cards(ob_cards)
            elif self.stop_num <= p <= 21:
                self.stop = True
            else:
                self.bust=True
                print("player {} bust! stop taking cards.".format(self.name))
                self.stop = True
                self.total_points = 0
        print("Result: {} with {}.".format(self.name, self.total_points))
           
        
    
class Player(Dealer):
    def __init__(self, stop_num=17, name='', total=100, multi=2):
        Dealer.__init__(self)
        self.total = total
        self.alive = True
        self.name = name
        self.bet = 10
        self.cards = np.array([])
        self.stop_num = stop_num
        self.multi=multi
        print("Player {} joined the game with {} dollars!".format(self.name, self.total))

    def make_bet(self, bet, ob_cards):
        if ob_cards.current_score >= 15:
            self.bet = bet*2*self.multi
            print("-"*60)
            print("{} has increased their bet to {}".format(self.name,self.bet))
            print("-"*60)
        elif ob_cards.current_score >= 5:
            self.bet=bet*self.multi
            print("-"*60)
            print("{} has increased their bet to {}".format(self.name, self.bet))
            print("-"*60)
        else:
            self.bet=bet
        if self.alive:
            if bet <= self.total:
                self.total -= bet
                self.bet = bet
            else:
                self.bet=self.total
                self.total = 0

    def check_money(self):
        if self.total <= 0:
            print("{} ran out of money!".format(self.name))
            self.alive = False
     
    def stop_by(self, ob_cards):
        Dealer.stop_by(self, ob_cards)
        
    def report_status(self):
        alive_status = "alive" if self.alive else "dead"
        print("Player {} ({}) has {} dollars!".format(self.name, alive_status, self.total))
        print("-"*60)

                 
    
#player = Player(100, 'Bob')
#player.take_cards(['10','A','K'])
#print(player.calc_points())
