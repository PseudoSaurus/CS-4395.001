from operator import truediv
import random

#Guessed letters global
pastAns = ''
score = 5

def start(self):

    global score, pastAns
    #point system and 1st word
    word = getWord(self)   

    print("We will now start the game. You will have 5 chances to guess a letter or the entire word!",
          "\nIf you would like to solve the word, please type in what you think the word is.",
          "\nDoing so will grant you points equal to the length of the word minus attepmts made + 3!")
   
   #Starting the game
    while True:

        #The player ranout of chances
        if score == 0:
            print("You have ran out of guess.\nThe correct word was:", word)
            print("Thank you for play and I hope to see you next time")
            break       

        #Getting the user's answer
        guess = get_Responce(word, score)
        
        #Exiting the game
        if guess == '!':
            print("Thank you for play! Hope to see you next time")
            break
        
        #seeing if the answer is right
        if process_game(guess, word):
            print("\n\nWell done! You have solved the word:", word)
            print("If you ever get tried of playing, just enter \'!\' as your next guess.\n\nI will now start a new round! Good luck!")
            
            #Getting a new random word
            word = getWord(self)

            #Clearing user's answers from last round
            pastAns = ''
    #End of WHILE loop
    
def getWord(words):
    RanIndex = random.randint(0, len(words) -1)
    return words[RanIndex]
#End of getWord(words)

def get_Responce(word, points):
    #Displays the mystory word
    gameShow(word)

    print("\nYou have {} remaining guesses!".format(points))
    #Getting the user's respoce
    guess = input("Guess a letter or the entire word\t")
    return guess
#End of get_Responce(word)

def process_game(guess, word):
    if len(guess) == len(word):
        return Wholeword_guess(guess, word)
    else:
        return singleword_guess(guess, word)

def gameShow(word):
    global pastAns    
    display_word = ''
    
    for letter in word:
        if pastAns.find(letter) > -1:
            # letter found
            display_word = display_word + letter
       
        else:
            # letter not found
            display_word = display_word + '-'
    print(display_word)
#End of gameShow

def Wholeword_guess(guessWord, word):
    global score, pastAns
    
    #seeing if the guess is correct
    if guessWord.lower() == word:
        score = score + (len(word) - len(pastAns)) + 3
        return True
    else:
        score -= 1
        return False
#End of Wholeword_guess(guessWord, word, score)


def singleword_guess(guess, word):
    global score
    global pastAns
    pastAns += guess.lower()

    #If the last letter was just solve
    if all_Letters_guessed(word):
        score += 1
        return True

    #Wrong answer means point is taken off
    if word.find(guess) == -1:
        score -= 1
    else:
        score += 1  #1 point is added for correct answers
    
    return False
#End of singleword_guess(guess, word, score)

def all_Letters_guessed(word):
    for letter in word:
        if pastAns.find(letter) == -1:
            return False
    #End of FOR loop
    return True
#End of all_Letters_guessed(word)