# Christopher Hunt
# CS 161
# Project 3 - Word Guessing Game

from hangman import Hangman
from bestOutOfThree import BestOutOfThree
from gameFunctions import gameIntializer, welcomeScreen

def main():
    """Main function"""
    game_on = True
    word_file = gameIntializer()
    while(game_on == True):
        players_mode = welcomeScreen()
        if (players_mode[1] == 1):
            game = BestOutOfThree(word_file, players_mode[0])
            game.gamePlay()

        elif(players_mode[1] == 2):
            game = Hangman(word_file, players_mode[0])
            game.gamePlay()

        elif(players_mode[1] == 3):
            print("Play again soon!")
            game_on = False

if __name__ == "__main__":
    main()