# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:20:44 2019

@author: gergo
"""
import numpy as np

from cards import value_cards

#print(value_cards)


class Dealer:
    def __init__(self):
        self.cards = np.array([])
        self.stop = False
        self.name = 'Dealer'
        
    def take_cards(self, ob_cards, num_cards=1):
        top = ob_cards.deck[:num_cards]
        ob_cards.deck = ob_cards.deck[num_cards:]
        self.cards = np.concatenate([self.cards, top])
        print("player {} taking {} cards ...".format(self.name, num_cards))
        print(self.cards, self.calc_points())
        
#        if type(cards) == list:
#            cards = np.array(cards)
#        self.cards = np.concatenate([self.cards, cards])
    
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
        
    def stop_by(self, ob_cards, by=17):
        while self.calc_points() < by and not self.stop:
           self.take_cards(ob_cards)
           if self.calc_points() > 21:
               print("player {} bust! stop taking cards.".format(self.name))
               self.stop = True
        print("Result: {} with {}.".format(self.name, self.calc_points()))
           
        
            
    
class Player(Dealer):
    def __init__(self, name='', total=100):
        Dealer.__init__(self)
        self.total = total
        self.alive = True
        self.name = name
        self.bet = 0
        self.cards = np.array([])
        print("Player {} joined the game with {} dollars!".format(self.name, self.total))
        
    def make_bet(self, bet):
        if self.alive:
            if bet <= self.total:
                self.total -= bet
                self.bet = bet
            else:
                self.total = 0
                self.bet = self.total

    def check_money(self):
        if self.total < 0:
            print("{} ran out of money!".format(self.name))
            self.alive = False
                 
    
#player = Player(100, 'Bob')
#player.take_cards(['10','A','K'])
#print(player.calc_points())
