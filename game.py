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
        
    def _deal_starting_hand(self) -> list:
        '''
        deal 2 cards from the deck, returns those cards as a list
        '''
        hand = [self.deck.pop() for i in range(2)]
    
    
    
    # interface methods
    
    def new_hand(self):
        '''
        deal a new round
        '''
        self._shuffle_deck()
        
        self.dealer = self._deal_starting_hand()
        self.player = self._deal_starting_hand()
        
    def get_dealer_cards(self, hide_card: bool = True) -> list:
        '''
        return the dealers cards, defaulting to hiding the first one
        '''
        if hide_card:
            return self.dealer[1:]
        
        return self.dealer
        
        