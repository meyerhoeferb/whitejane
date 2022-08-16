'''
simple blackjack implementation
'''

import random

class BlackJack():
    def __init__(self):
        self.deck = random.shuffle(range(52))
        
        self.dealer = []        # dealers cards
        
        self.player = []        # player cards
        
        
    # internal methods   
        
    def _shuffle_deck(self):
        '''
        reset the deck
        '''
        self.deck = random.shuffle(range(52))
        

        