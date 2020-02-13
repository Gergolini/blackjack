from player import Dealer, Player
from cards import Cards

class Game:
    def __init__(self, player_list, ob_cards):
        self.player_list = player_list
        self.ob_cards = ob_cards
        
    def initialize(self):
        self.ob_cards.generate_deck()

    def run_game(self):
        for i, player in enumerate(self.player_list):
            if i != 0:
                player.check_money()
                payer.make_bet(10)
            player.init_cards(self.ob_cards)

        for player in self.player_list[1:]:
            player.stop_by(self.ob_cards)
            cards.check_cards()
        self.player_list[0].stop_by(self.ob_cards)

    def payout(self):
        dp = self.player_list[0].total_points
        dbj = self.player_list[0].isbj
        rate = 0.0
        for player in self.player_list[1:]:
            if not player.bust:
                pp = player.total_points
                pbj = player.isbj
                if (dbj and pbj) or (not dbj and not pbj and pp==dp):
                    rate = 1.0
                elif pbj and not dbj:
                    rate = 2.5
                elif (not dbj and not pbj and pp>dp):
                    rate = 2.0
                print(player.name, rate)
                player.total = player.total + (rate*player.bet)

    def loop_game(self, n=100):
        """
        :param: n [int] number of rounds the game is simulated
        """
        for i in range(n):
            self.run_game()
            self.payout()
            for j, player in enumerate(self.player_list):
                if j != 0:
                    player.report_status()
                player.clear_cards()






dealer = Dealer()
gergo = Player('Gergo', 100.0)
qi = Player('Qi', 100.0)
players = [Dealer(), gergo, qi]
ob_cards = Cards(4)
game = Game(players, ob_cards)
game.initialize()
game.loop_game(50)
