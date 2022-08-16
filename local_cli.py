'''
cli for playing blackjack locally, no server

only single player
'''
from blackjack import BlackJack

def cli():
    #make game object
    bj = BlackJack()
  
    #gameplay loop  
    play = True
    while play:
        play = main_menu()
        if play:
            # play the hand
            pass
    
    print("Thanks for playing!")
    
    
def main_menu() -> bool:
    '''
    main menu, prompts for starting a hand or quitting
    
    returns true if starting a hand, false otherwise
    '''
    
    while True:
        ans = input("Start a hand? [y/n]: ")
        if ans == 'y':
            return True
        if ans == 'n':
            return False
        else:
            print("Unrecognized input")


if __name__ == "__main__":
    cli()