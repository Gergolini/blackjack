from player import Dealer, Player
from cards import Cards
import sys

class Game:
    def __init__(self, player_list, ob_cards):
        self.player_list = player_list
        self.ob_cards = ob_cards
        
    def initialize(self):
        self.ob_cards.generate_deck()
        print("hello")

    def run_game(self):
        self.ob_cards.deck_status()
        self.ob_cards.check_cards()
        
        for i, player in enumerate(self.player_list):
            if i != 0 and player.alive:
                player.check_money()
                player.make_bet(10)

        self.player_list[0].init_cards(self.ob_cards)

        for player in self.player_list[1:]:
            if player.alive:
                player.init_cards(self.ob_cards)
                player.stop_by(self.ob_cards)
        self.player_list[0].stop_by(self.ob_cards)

    def payout(self):
        dp = self.player_list[0].total_points
        dbj = self.player_list[0].isbj
        for player in self.player_list[1:]:
            if player.alive:
                rate = 0.0
                if not player.bust:
                    pp = player.total_points
                    pbj = player.isbj
                    if (dbj and pbj):
                        rate = 1.0
                    elif ((not dbj) and (not pbj) and (pp==dp)):
                        rate = 1.0
                    elif pbj and not dbj:
                        rate = 2.5
                    elif ((not dbj) and (not pbj) and (pp>dp)):
                        rate = 2.0
                    player.total = player.total + (rate*player.bet)

    def loop_game(self, n=100):
        """
        :param: n [int] number of rounds the game is simulated
        """
        for i in range(n):
            print("game {}/{} started ...".format(i+1, n))
            self.run_game()
            self.payout()
            for j, player in enumerate(self.player_list):
                if j != 0:
                    player.report_status()
                player.clear_cards()

a=0
b=0
for i in range (1):
    dealer = Dealer()
    gergo = Player(18,'Gergo', 100.0)
    qi = Player(19,'Qi', 100.0)
    # print(dealer.stop_num, gergo.stop_num, qi.stop_num)
    players = [dealer, gergo, qi]
    ob_cards = Cards(4)
    game = Game(players, ob_cards)
    game.initialize()
    game.loop_game(50)
    if players[1].total>=100:
        a=a+1
    if players[2].total>=100:
        b=b+1
print ("Gergo got a surplus {} times!".format (a))
print ("Qi got a surplus {} times".format(b))
