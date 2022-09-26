from asyncio.windows_events import NULL
from queue import Empty
from HLPfile import *
from WordguessGame import *
import sys

def printDic(DICT, list):
    breaker = 50 
        
    #Looping to the Ascend_NounDic
    for key,value in DICT.items():
        #Printing the element
        print(key, ':', value)

        #adding the word to the list
        list.append(key) 

        breaker -= 1
        #Stopping at element 50 if possible 
        if breaker == 0:
            break

if __name__ == '__main__':

    #Making sure there is something in argv
    if len(sys.argv) > 2 or len(sys.argv) < 0:
        print("You need to enter a valid filename. \nPlease try again.")
        quit()
        
    #Storing the filename from the console
    filename = sys.argv[1]
    print("I will now read ", filename)

    #Reading the file and tokenizing it
    Tokentext = tokenProcess(filename)
    
    #calculating the Lex. divi.
    Tokentext = calcula_LexDiv(Tokentext)

    #Seperating the nouns from Tokentext
    gameWords, Noun_gameWords = Deep_tokenProcess(Tokentext)

    #Making a dictionary of decen common Nouns
    nounDic = {index:Noun_gameWords.count(index) for index in gameWords}
    #sorting nounDic from largest to smallest
    Ascend_NounDic = {key: val for key, val in sorted(nounDic.items(), key = lambda ele: ele[1], reverse = True)}

    #Making a dictionary for all words
    allWordsDic = {index:gameWords.count(index) for index in Tokentext}
    #sorting nounDic from largest to smallest
    Ascend_WordsDic = {key: val for key, val in sorted(allWordsDic.items(), key = lambda ele: ele[1], reverse = True)}

    #Words of the game 
    everyWord = []
    #Showing my findings
    print("\nThe 50-ish popular nouns are")
    printDic(Ascend_NounDic, everyWord)    

    print("\nThe 50-ish popular all time words are")
    printDic(Ascend_WordsDic, everyWord)

    #Commensing the game
    start(everyWord)
#End of __name__ == '__main__'

