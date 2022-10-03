from programUno_DictionCreation import *
import pickle
import math
from nltk import word_tokenize
from nltk import ngrams
import os

######################### Start of loadData #########################
def loadData():
    #for reading also binary mode is important
    dbfile_Unigram = open('DBfile_UniDic.pickle', 'rb')     
    dbfile_Bigram = open('DBfile_BiDic.pickle', 'rb')     

    #Unloading the pickles
    db_Unigram = pickle.load(dbfile_Unigram)
    db_Bigram = pickle.load(dbfile_Bigram)

    #Making sure everything the pickle is not empty
    for keys in db_Unigram:
        print(keys, '=>', db_Unigram[keys])

    for keys in db_Bigram:
        print(keys, '=>', db_Bigram[keys])      

    dbfile_Unigram.close()
    dbfile_Bigram.close()

    return db_Unigram, db_Bigram
######################### End of loadData #########################

################ Start of readFiles ##############################
def readFiles(fileName):
    
    if os.path.isfile(fileName):
        #open text file in read mode
        text_file = open(fileName, "r", encoding= 'Latin1')

        #Reading the whole file w/ no \n
        data = text_file.read()   #Should be in string

        #closing file
        text_file.close()

        return data 
    else:
        quit
#End of reader loop
################ End of readFiles ##############################


######################### Start of compute_Prob #########################
def compute_Prob(line, DB_Unigram, DB_Bigram, VocabNum):
     
    #Making the unigram and bigram of the test
    Unigram_Test = word_tokenize(line)
    Bigram_Test = list(ngrams(Unigram_Test, 2))
    
    p_Goodturn = 1  # calculate p using a variation of Good-Turing smoothing
    p_laplace = 1   # calculate p using Laplace smoothing
    p_log = 0      # add log(p) to prevent underflow

    numorator = len(DB_Bigram)

    for bigram in Bigram_Test:
        numorator = DB_Bigram[bigram] if bigram in DB_Bigram else 0
        n_Goodturn = DB_Bigram[bigram] if bigram in DB_Bigram else 1/VocabNum
        denominator = DB_Unigram[bigram[0]] if bigram[0] in DB_Unigram else 0
            
        if denominator == 0:
            p_Goodturn = p_Goodturn * (1 / VocabNum)
        else:
            p_Goodturn = p_Goodturn * (n_Goodturn / denominator)

        p_laplace = p_laplace * ((numorator + 1) / (denominator + VocabNum))

    

    #Outputting the results 
    print("\nProbability with simplified Good-Turing is ", p_Goodturn)
    print("Probability with laplace smoothing is ", p_laplace)

    return p_laplace
######################### End of compute_Prob #########################

def Unigram_VocabSum(DB_Unigram):
    sum = 0
    
    for key in DB_Unigram:
        sum = sum + len(DB_Unigram[key])
    
    return sum

######################### Start of main() #########################
if __name__ == '__main__':
    
    lineCount = 0
    
    #Setting the names for our test and solution file.
    Lang_Test = "LangId.test"

    print(Lang_Test)
    #Reading and unloading the pickel files
    DB_Uni, DB_Bi = loadData()

    #Creating our answer file
    myFile = open("SilvanoG_LangGuess.txt", "w")

    #Getting the total vocab of all 3 unigram dictionaries
    VocabNum = Unigram_VocabSum(DB_Uni)

    for line in open(Lang_Test, 'r'):
        sentence = line.strip('\n')
        highest_prob = 1
      
        for key in DB_Bi:
            print("\nLets go through the {} dictornary".format(key))

            Lang_Probability =compute_Prob(sentence, DB_Uni[key], DB_Bi[key], VocabNum)
            
            if highest_prob > Lang_Probability:
                highest_prob = Lang_Probability
                choiceLang = key
                
        #Write a file w/ incrementing num for current line 
        # and choiceLang next to it.
        inputstring ="{}  {}\n".format(lineCount,choiceLang)
        myFile.write(inputstring)

        #Increment the line count
        lineCount = lineCount+1
    #End of Outer FOR loop
    myFile.close()

    print("\n\nContent from Solution file\tvs\tContent from my file:\n")


    lineAns = open("LangId.sol", 'r')
    line1 = lineAns.readlines()

    lineRespond = open("SilvanoG_LangGuess.txt", 'r')
    line2 = lineRespond.readlines()

    for index in range(300):
        lang1 = line1[index]
        lang1 = lang1.strip('\n')

        lang2 = line2[index]
        lang2 = lang2.strip('\n')
        
        print(lang1,"\t\t\t\t", lang2)
######################### End of main() #########################


