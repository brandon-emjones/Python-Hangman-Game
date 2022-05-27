#Filename: hangman.py
#Creator: Brandon Jones
#Purpose: contains the Hangman_Game Class used by app.py

from hangman_pkg import phrases
import random

#class from which all objects for game are created.
class Hangman_Game:
    def __init__(self):
        self.rand_int = random.randint(0, len(phrases.list_of_phrases) - 1)
        self.game_phrase = list(phrases.list_of_phrases[self.rand_int])
        self.char_count = len(self.game_phrase)
        self.partial_phrase = []
        self.wrong_guess_list = []
        self.set_blank_phrase()
        self.wrong_guess_limit = 6
        self.wrong_guess_count = 0
        self.guess_count = 0
        self.hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    # method for printing the title and instructions for the game.
    def print_intro(self):
        print("""
 __  __     ______     __   __     ______     __    __     ______     __   __        ______     ______     __    __     ______    
/\ \_\ \   /\  __ \   /\ "-.\ \   /\  ___\   /\ "-./  \   /\  __ \   /\ "-.\ \      /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   
\ \  __ \  \ \  __ \  \ \ \-.  \  \ \ \__ \  \ \ \-./\ \  \ \  __ \  \ \ \-.  \     \ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\   
 \ \_\ \_\  \ \_\ \_\  \ \_\\\\"\_\  \ \_____\  \ \_\ \ \_\  \ \_\ \_\  \ \_\\\\"\_\     \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\ 
  \/_/\/_/   \/_/\/_/   \/_/ \/_/   \/_____/   \/_/  \/_/   \/_/\/_/   \/_/ \/_/      \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/ 


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++                  Welcome to the HANGMAN GAME!                       ++
++     Enter your letter guesses to fill in the famous movie line.     ++
++ But be carefull! 6 wrong guesses and your HANGMAN gets the noose ;) ++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""")

    # method that prints when the user wins.
    def print_win(self):
        print("""
 __  __     ______     __  __        __     __     __     __   __    
/\ \_\ \   /\  __ \   /\ \/\ \      /\ \  _ \ \   /\ \   /\ "-.\ \   
\ \____ \  \ \ \/\ \  \ \ \_\ \     \ \ \/ ".\ \  \ \ \  \ \ \-.  \  
 \/\_____\  \ \_____\  \ \_____\     \ \__/".~\_\  \ \_\  \ \_\\\\"\_\ 
  \/_____/   \/_____/   \/_____/      \/_/   \/_/   \/_/   \/_/ \/_/ 
        """)

    # method that prints when the user loses.
    def print_lose(self):
        print("""
 __  __     ______     __  __        __         ______     ______     ______    
/\ \_\ \   /\  __ \   /\ \/\ \      /\ \       /\  __ \   /\  ___\   /\  ___\   
\ \____ \  \ \ \/\ \  \ \ \_\ \     \ \ \____  \ \ \/\ \  \ \___  \  \ \  __\   
 \/\_____\  \ \_____\  \ \_____\     \ \_____\  \ \_____\  \/\_____\  \ \_____\ 
  \/_____/   \/_____/   \/_____/      \/_____/   \/_____/   \/_____/   \/_____/
        """)

    # method that prints a border to keep each user turn seperated visually
    def print_border(self):
        print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """)

    # method that prints the correct hangman image to screen from list based on wrong_guess_count
    def print_hangman(self):
        print(self.hangman_pics[self.wrong_guess_count])

    # method that prints wrong guesses to screen for user reference
    def print_wrong_guesses(self):
        print("Wrong Guesses:", self.wrong_guess_list)

    # method that builds a blanked list of characters matching the size of the game_phrase list.
    def set_blank_phrase(self):
        for char in self.game_phrase:
            if char == " ":
                self.partial_phrase.append("  ")
            elif char == ",":
                self.partial_phrase.append(",")
            elif char == "'":
                self.partial_phrase.append("'")
            elif char == ".":
                self.partial_phrase.append(".")
            elif char == "!":
                self.partial_phrase.append("!")
            else:
                self.partial_phrase.append("_")

    # method that prints the partial_list on screen each turn
    def print_partial_phrase(self):
        print("")
        for char in self.partial_phrase:
            print(char, end="")

    # method that prints the complete phrase on screen at the end of the game.
    def print_full_phrase(self):
        print("\nCorrect Phrase: ", end="")
        for char in list(phrases.list_of_phrases[self.rand_int]):
            print(char, end="")

    # method and that checks and validates user's guess.
    def check_guess(self):
        guess = input("\n\nWhat letter do you think is in the movie line? ")

        self.print_border()

        # if/else that validates that guess is 1 character long and is alphabetical.
        if len(guess) != 1 or guess.isalpha() == False:
            print(
                "\nInvalid Guess. Your guess must be a single character Aa-Zz. Please Try Again.")
            self.check_guess()
            return

        # if/else that validates that the character in guess has not already been used.
        if guess.upper() in self.partial_phrase or guess.upper() in self.wrong_guess_list:
            print(
                "\nInvalid Guess. You have already guessed this letter. Please Try Again.")
            self.check_guess()
            return

        self.guess_count += 1

        # if/else that checks if guess is in the game_phrase
        if guess.upper() in self.game_phrase or guess.lower() in self.game_phrase:
            # if true, iterate through game_phrase
            for char in self.game_phrase:
                # compares guess to index of game_phrase
                if char.upper() == guess.upper():
                    # if they match, copy index value in game_phrase to same index position in partial_phrase
                    self.partial_phrase[self.game_phrase.index(char)] = guess.upper()
                    # replace index value in game_phrase with unique character. This allows the index method in
                    # the previous line to find the next index position of the guess in situatuions where there
                    # are multiples of that value in the game_phrase.
                    self.game_phrase[self.game_phrase.index(char)] = "@"
            print("\nGood Guess! Your letter has been added to the phrase!")
        else:
            # if false, increment wrong_guess_count and add guess to wrong_guess_list
            self.wrong_guess_count += 1
            self.wrong_guess_list.append(guess.upper())
            if self.wrong_guess_count < self.wrong_guess_limit:
                print("\nSorry! Incorrect Guess! Your hangman is in danger!")
            else:
                print("\nSorry! Incorrect Guess! Your hangman is DEAD!")

    # method that checks partial_phrase to see if it has been completed.
    def check_phrase(self):
        if "_" not in self.partial_phrase:
            return True
        else:
            return False

    # method that asks the user if they would like to play again.
    def play_again(self):
        answer = input(
            "\n\nWould you like to play again (Y: Yes / Anything Else: No): ")
        if answer.upper() == "Y":
            return True
        else:
            return False
