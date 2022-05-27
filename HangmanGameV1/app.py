#Filename: app.py
# Creator: Brandon Jones
# Purpose: main app that runs the Hangman Game.

from hangman_pkg import hangman

# Main loop that will run the game at least one time.
while True:
    newgame = hangman.Hangman_Game()
    newgame.print_intro()

    # Nested loop that runs the main actions of the game until the player wins or loses
    while newgame.check_phrase() is False and newgame.wrong_guess_count < newgame.wrong_guess_limit:
        newgame.print_hangman()
        newgame.print_wrong_guesses()
        newgame.print_partial_phrase()
        newgame.check_guess()

    # if/else that determines if the previous loop ended because the user won or lost and prints message.
    if newgame.wrong_guess_count == newgame.wrong_guess_limit:
        newgame.print_lose()
    else:
        newgame.print_win()

    # prints the complete phrase on the screen for the user to see at the end of the game.
    newgame.print_full_phrase()

    # if/else to determine if the user would like to play again.
    if newgame.play_again() == False:
        print("\nGoodbye!")
        break
