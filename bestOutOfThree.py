from PyDictionary import PyDictionary
import random

class BestOutOfThree:

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
 
    def gamePlay(self):
        """Best Out of Three.
        Up to three players, the computer picks a random word and gives the players the definition.
        Players take turns guessing the word. After each round the scores are shown.
        After three rounds the highest score is reported as the winner, if there is a tie then a tie is reported."""

        print("\n####Best Out Of Three####")
        score = [0]*self.players
        answers = [str]*3
        game_on = True
        while(game_on == True):
            for round in range(0,3):
                word_and_def = self.definedWord()
                secret_word = word_and_def[0]
                meaning = word_and_def[1]
                answers[round] = secret_word
                print(meaning)
                for player in range(1, self.players+1):
                    guess = input(f"Player {player}: ").lower()
                    if (guess == secret_word):
                        score[player-1] += 1
                    else:
                        pass
                print(f"Score: {score}")
            high_score = max(score)
            winner =score.index(high_score)+1
            tie = score.count(high_score)
            if (tie > 1):
                print(f"Final Scores: {score}\nThe correct answers were: {answers[0]}, {answers[1]}, and {answers[2]}\nThis game was a tie!\n\n")
            else:
                print(f"Final Scores: {score}\nThe correct answers were: {answers[0]}, {answers[1]}, and {answers[2]}\nThe winner is Player {winner}\n\n")
            game_on = False

