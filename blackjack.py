'''
simple blackjack implementation
'''

import random

class BlackJack():
    def __init__(self):
        self.deck = self._shuffle_deck()
        
        self.hands = []         # 2d array tracking dealer and player hands
        
        self.dealer = 0             # dealer will be the first player
        self.current_player = 1     # track player whose action it is
        
        
    # internal methods   
        
    def _shuffle_deck(self) -> list[int]:
        '''
        returns a shuffled deck as a list of ints
        '''
        return random.shuffle([x for x in range(52)])
        

        