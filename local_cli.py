"""
cli for playing blackjack locally, no server

only single player
"""
from blackjack import BlackJack

CARD_MAP = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def cli():
    # make game object
    bj = BlackJack()

    # gameplay loop
    play = True
    while play:
        play = main_menu()
        if play:
            # deal hand
            bj.start_game()
            # player turn loop
            while bj.current_player <= bj.num_players:
                print(f"YOUR HAND: {get_player_hand(bj)}")
                action = player_menu()

                # handle action
                if action == "stand":
                    break

    print("Thanks for playing!")


def card_int_to_string(card: int) -> str:
    """
    convert card from integer to string representation
    """
    return CARD_MAP[card % 13]


def get_player_hand(bj: BlackJack) -> str:
    """
    gets the current players hand from the game object and displays it
    """
    hand = bj.get_player_hand()

    hand_str = [card_int_to_string(c) for c in hand]

    return " ".join(hand_str)


def player_menu() -> str:
    """
    displays the options the player can take and returns it as a string
    """
    print("player menu goes here")

    return "stand"


def main_menu() -> bool:
    """
    main menu, prompts for starting a hand or quitting

    returns true if starting a hand, false otherwise
    """

    while True:
        ans = input("Start a hand? [y/n]: ")
        if ans == "y":
            return True
        if ans == "n":
            return False
        else:
            print("Unrecognized input")


if __name__ == "__main__":
    cli()
