from player import Dealer, Player
from cards import Cards
from utils import timer

class Game:
    def __init__(self, player_list, ob_cards):
        self.player_list = player_list
        self.ob_cards = ob_cards
    
    @timer
    def initialize(self):
        self.ob_cards.generate_deck()
        for i, player in enumerate(self.player_list):
            if i != 0:
                player.check_money()
                player.make_bet(10)
            player.init_cards(self.ob_cards)

    @timer
    def run_game(self):
        for player in self.player_list[1:]:
            player.stop_by(self.ob_cards)
        self.player_list[0].stop_by(self.ob_cards)

    @timer
    def payout(self):
        dp = self.player_list[0].total_points
        dbj = self.player_list[0].isbj
        rate = 0.0
        for player in self.player_list[1:]:
            if player.bust==True:
                pass
            else:
                pp = player.total_points
                pbj = player.isbj
                if dbj and pbj or (not dbj and not pbj and pp==dp):
                    rate = 1.0
                elif pbj and not dbj:
                    rate = 2.5
                elif (not dbj and not pbj and pp>dp):
                    rate = 2.0
                player.total = player.total + (rate*player.bet)


    """
    HW: fix the bust first bug, lose the game immediately after bust (including your bet).
    """





dealer = Dealer()
gergo = Player('Gergo', 100.0)
qi = Player('Qi', 100.0)
players = [Dealer(), gergo, qi]
ob_cards = Cards(4)
game = Game(players, ob_cards)
game.initialize()
game.run_game()
game.payout()
for player in players[1:]:
    player.report_status()
