from player import Dealer, Player
from cards import Cards

class Game:
    def __init__(self, player_list, ob_cards):
        self.player_list = player_list
        self.ob_cards = ob_cards
        
    def initialize(self):
        self.ob_cards.generate_deck()
        for i, player in enumerate(self.player_list):
            if i != 0:
                player.check_money()
                player.make_bet(10)
            player.take_cards(self.ob_cards, num_cards=2)
            
            
    def run_game(self):
        for player in self.player_list[1:]:
            player.stop_by(self.ob_cards)
        self.player_list[0].stop_by(self.ob_cards)
    
    def payout(self):
        for player in self.player_list[1:]:
            if player.total_points > self.player_list[0].total_points:
                player.total = player.total+(2*player.bet)
                
    """
    HW: debug the error in our code and add the check for blackjack in payout.
    """
                
            
            
            

dealer = Dealer()
gergo = Player('Gergo', 100)
qi = Player('Qi', 100)
players = [Dealer(), gergo, qi]
ob_cards = Cards(4)
game = Game(players, ob_cards)
game.initialize()
game.run_game()
game.payout()
for player in players[1:]:
    player.report_status()