"""
cli for playing blackjack locally, no server

only single player
"""
from termcolor import colored, cprint
from blackjack import BlackJack


CARD_MAP = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
POINTS_MAP = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


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
            game_over = False
            while bj.current_player <= bj.num_players and not game_over:
                print(f"YOUR HAND: {player_hand_to_string(bj)}")
                action = player_menu()

                # handle action
                if action == "STAND":
                    break
                elif action == "HIT":
                    hit(bj)
                    # check for bust

    print("Thanks for playing!")


def hit(bj: BlackJack):
    """
    make a hit call to the blackjack object
    """
    bj.hit()


def card_int_to_string(card: int) -> str:
    """
    convert card from integer to string representation
    """
    return CARD_MAP[card % 13]


def player_hand_to_string(bj: BlackJack) -> str:
    """
    gets the current players hand from the game object and displays it
    """
    hand = bj.get_player_hand()

    hand_str = [card_int_to_string(c) for c in hand]

    return colored(" ".join(hand_str), "blue")


def player_menu() -> str:
    """
    displays the options the player can take and returns it as a string
    """
    actions = ["HIT", "STAND"]
    actions_to_print = colored("\t".join(actions), "green")
    print(f"PLAYER ACTIONS: {actions_to_print}")
    while True:
        p_action = input("Select an action: ").upper()
        if p_action not in actions:
            print("unrecognized command")
            continue

        return p_action


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


# colored print methods
def print_green(s):
    return cprint(s, "green")


if __name__ == "__main__":
    cli()
