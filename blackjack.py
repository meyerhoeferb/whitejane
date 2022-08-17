"""
simple blackjack implementation
"""

import random


class BlackJack:
    def __init__(self):
        self.deck = self._shuffle_deck()

        self.hands = []  # 2d array tracking dealer and player hands

        self.num_players = 0  # gets set every time a hand starts

        self.dealer = 0  # dealer will be the first player
        self.current_player = 1  # track player whose action it is

    # internal methods

    def _shuffle_deck(self) -> list[int]:
        """
        returns a shuffled deck as a list of ints
        """
        deck = [x for x in range(52)]
        random.shuffle(deck)
        return deck

    def _draw_card(self) -> int:
        """
        draw card from deck
        """
        return self.deck.pop()

    def _deal_starting_hand(self) -> list[int]:
        """
        deal a starting hand of 2 cards
        """
        return [self._draw_card(), self._draw_card()]

    # interface methods
    def start_game(self, num_players: int = 1):
        """
        deal a new hand for however many players + the dealer

        defaults to 1 player
        """
        self.deck = self._shuffle_deck()
        self.num_players = num_players

        # one more than num players (for dealer)
        for i in range(num_players + 1):
            self.hands.append(self._deal_starting_hand())

    def get_player_hand(self, player: int = 0) -> list[int]:
        """
        returns the specified players hand as a list of ints
        defaults to current player, cannot be used to get dealer hand
        """
        if player > self.num_players:
            raise Exception(f"Tried to get player {player}s hand, but only {self.num_players} in game")

        if player == 0:
            return self.hands[self.current_player]
        else:
            return self.hands[player]
