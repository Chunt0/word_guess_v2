def gameIntializer():

    """Create a PyDictionary and reads text file containing list of words."""

    file = []
    with open("/home/chunt/VScode/Python/CS161/project4/words.txt", "r") as f:
        file=f.readlines()
    return file

def isInt(string):

    """Checks if the user input is an integer and returns that integer. Else print error"""    

    try:
        integer = int(input(string))
        if (integer > 0 and integer < 4):
            return integer
        else:
            print("ERROR::ENTER A 1, 2, OR  3")
            isInt(string)
    except:
        print("ERROR::ENTER A 1, 2, OR 3")
        isInt(string)

def welcomeScreen():

    """Welcomes players and asks how many players
    Ask which game mode: 1. Best of three 2. Hangman 3. Speed"""

    p_m = [0,0]
    print("####### KNOW YOUR WORDS #######")
    p_m[1] = isInt("Pick a mode\n1. Best out of three\n2. Hangman\n3. Quit\nMODE::")
    if (p_m[1] == 3):
        return p_m
    else:
        p_m[0] = isInt("Number of Players:") 
    return p_m
