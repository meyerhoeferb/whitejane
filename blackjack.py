"""
simple blackjack implementation
"""

import random


class BlackJack:
    def __init__(self):
        self.deck = self._shuffle_deck()

        self.hands = []  # 2d array tracking dealer and player hands
        self.scores = []  # scores for all players, updated whenever something happens to change it

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

    def _calculate_score(self, player: int) -> int:
        """
        calculate the score for the given player
        """
        cards = [c % 13 for c in self.hands[player]]
        score = 0
        num_aces = 0  # track how many aces this player has to can calculate accurately
        for c in cards:
            # cards that just add their value (which is one greater than what c is)
            if c > 0 and c < 11:
                score += c + 1
            elif c == 0:
                # aces add 11, at end will subtract if needed
                num_aces += 1
                score += 11
            else:
                # all other cases are 10 points
                score += 10

        # turn 11s in to 1s if necessary and possible
        while score > 21 and num_aces > 0:
            score -= 10
            num_aces -= 1

        return score

    # interface methods

    def start_game(self, num_players: int = 1):
        """
        deal a new hand for however many players + the dealer

        defaults to 1 player
        """
        self.deck = self._shuffle_deck()
        self.current_player = 1
        self.num_players = num_players

        # one more than num players (for dealer)
        for i in range(num_players + 1):
            self.hands.append(self._deal_starting_hand())
            self.scores.append(self._calculate_score(i))

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

    def hit(self):
        """
        draw a card for the current player
        """
        if len(self.deck) == 0:
            raise Exception("Tried to draw from empty deck")

        self.hands[self.current_player].append(self._draw_card())
        self.scores[self.current_player] = self._calculate_score(self.current_player)

    def get_player_score(self, player: int = 0):
        """
        returns the specified players current score
        defaults to current player, cannot be used to get dealer score
        """
        if player > self.num_players:
            raise Exception(f"Tried to get player {player}s hand, but only {self.num_players} in game")

        if player == 0:
            return self.scores[self.current_player]
        else:
            return self.scores[player]

    def end_turn(self):
        """
        ends the current players turn
        """
        self.current_player += 1
