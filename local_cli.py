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
        print("\n\n\n\n")
        play = main_menu()
        if play:
            # deal hand
            bj.start_game()

            # player turn loop
            while bj.current_player <= bj.num_players:
                turn_over = False
                print_blue(f"\nYOUR HAND: {player_hand_to_string(bj)} ({player_score_to_string(bj)})")
                action = player_menu()

                # handle action
                if action == "STAND":
                    turn_over = True
                elif action == "HIT":
                    hit(bj)
                    # check for bust
                    if check_for_bust(bj):
                        print_on_red(bust_message(bj))
                        turn_over = True

                # check if the turn has finished
                if turn_over:
                    end_player_turn(bj)

    print("Thanks for playing!")


def end_player_turn(bj: BlackJack):
    """
    makes the call to bj object to end current players turn
    """
    bj.end_turn()


def check_for_bust(bj) -> bool:
    """
    returns true if the current player busted
    """
    if bj.get_player_score() > 21:
        return True

    return False


def bust_message(bj):
    """
    returns the message to display on bust as a string
    """
    return f"BUSTED! YOUR HAND: {player_hand_to_string(bj)} ({player_score_to_string(bj)})"


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
    gets the current players hand from the game object and converts it to human readable
    """
    hand = bj.get_player_hand()

    hand_str = [card_int_to_string(c) for c in hand]

    return " ".join(hand_str)


def player_score_to_string(bj: BlackJack) -> str:
    """
    get the current players score as a string
    """
    score = bj.get_player_score()
    return str(score)


def player_menu() -> str:
    """
    displays the options the player can take and returns it as a string
    """
    actions = ["HIT", "STAND"]
    actions_to_print = "\t".join(actions)
    print(f"PLAYER ACTIONS:")
    print_green(actions_to_print)
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
    print(colored(s, "green"))


def print_blue(s):
    print(colored(s, "blue"))


def print_yellow(s):
    print(colored(s, "yellow"))


def print_on_red(s):
    print(colored(s, on_color="on_red"))


if __name__ == "__main__":
    cli()
