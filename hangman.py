import random
from PyDictionary import PyDictionary
from gameFunctions import isInt


class Hangman:
    def __init__(self, file, players):
        self.file = file
        self.players = players

    def definedWord(self):

        """A random number is selected. This will be used to select a word from the imported words.txt file
        A list is created to hold the random word and a dictionary definition using the PyDictionary module.
        An attempt is made to weed out errors between the words.txt file and PyDictionary. This did not work."""
        dictionary = PyDictionary()
        rand_num = random.randrange(1,10000)
        word_def = [str,{str:str}]
        word_def[0] = self.file[rand_num].strip('\n')
        word_def[1] = dictionary.meaning(word_def[0])
        return word_def
    
    def selectionMenu(self, word_def):
        """Number of players and word selection"""
        secret_word_def =[str, {str:str}, int]
        if (self.players > 1):
            choice = isInt("Would you like to:\n1. Enter your own word\n2. Let the computer choose\nChoice: ")
            if (choice == 1):
                secret_word_def[0] = input("Enter your secret word: ").lower()
                secret_word_def[1] = input("Enter your word's definition: ")
                secret_word_def[2] = len(secret_word_def[0])
            else:
                secret_word_def[0] = word_def[0]
                secret_word_def[1] = [word_def[1]]
                secret_word_def[2] = len(word_def[0])          
        else:
            secret_word_def[0] = word_def[0]
            secret_word_def[1] = [word_def[1]]
            secret_word_def[2] = len(word_def[0])
        return secret_word_def

    def gamePlay(self):
        """Begin Hangman"""
        word_def =self.definedWord()
        secret_word = self.selectionMenu(word_def)
        print(secret_word[2])

        guess_array = [[str], int, int]
        guess_array[0] =["*"]*secret_word[2]
        guess_array[1] = 6
        guess_array[2] = 0
        print(f"\n####HANGMAN####\n\nYou have {guess_array[1]} guesses. Type 'guess' to give your final answer.\nUse one of your guesses to receive the definition by typing 'def'\n\nYour word is {secret_word[2]} characters long.\n")
        print(guess_array[0])

        """Guessing loop"""
        while(guess_array[2] < guess_array[1]):
            correct_guess = False
            character= input(f"{guess_array[1] - guess_array[2]} incorrect guesses left: ")
            if (character == "guess"):
                break
            elif (character == "def"):
                print(secret_word[1])
                guess_array[2] += 1
                correct_guess = True
            else:
                for index, char in enumerate(secret_word[0]):
                    if (character == char):
                        guess_array[0][index] = character
                        correct_guess = True
                    else:
                        pass
            print(guess_array[0])
            if not (correct_guess):
                guess_array[2] += 1
        final_guess = input("Your final guess: ")
        
        """Build set of missed characters"""
        missing_char_set = set()
        for index, char in enumerate(secret_word[0]):
            if (char != (guess_array[0][index])):
                missing_char_set.add(char)
            else:
                pass
       
        if (final_guess == secret_word[0]):
            print(f"You won!\nThe word was '{secret_word[0]}'.\n\n")
        else:
            print(f"You lost....\nYou should have guessed these letters: {missing_char_set}\nThe secret word was {secret_word[0]}\n\n")