from nltk import word_tokenize
from nltk import ngrams
import pickle
import os

################ Start of readFiles ##############################
def readFiles(fileName):
    
    if os.path.isfile(fileName):
        #open text file in read mode
        text_file = open(fileName, "r", encoding= 'Latin1')

        #Reading the whole file w/ no \n
        data = text_file.read().replace("\n","")    #Should be in string

        #closing file
        text_file.close()

        return data 
    else:
        quit
#End of reader loop
################ End of readFiles ##############################

################ Start of nGram_Dict ##############################
def nGram_Dict(Token, Filestrings):

    #Creating the Unigram List
    #Unigram = list(ngrams(Token,1))
    Unigram = list(ngrams(Token,1))
    
    #Creating the Unigram Dictionary from the list
#    Unigram_Dic = {ele:Token.count(ele) for ele in set(Unigram)}
    Unigram_Dic = {}
    for Unigram in set(Unigram):
         Unigram_Dic[Unigram[0]] = Filestrings.count(Unigram[0])
    
    count = 1
    for uni in Unigram_Dic.keys():
        print(uni, '->', Unigram_Dic[uni])
        count += 1
        if count > 5:
            break

    #Creating the Bigram list
    Bigram = list(ngrams(Token, 2))

    #Creating the Bigram Dictionary from the list
#    Bigram_Dic = {ele:Bigram.count(ele) for ele in set(Bigram)}
    Bigram_Dic = {}
    for bigram in set(Bigram):
        if bigram not in Bigram_Dic:
            bi = bigram[0] + ' ' + bigram[1]
            Bigram_Dic[bi] = Filestrings.count(bi)
        
    count = 1
    for bi in Bigram_Dic.keys():
        print(bi, '->', Bigram_Dic[bi])
        count += 1
        if count > 10:
            break       

    return Unigram_Dic, Bigram_Dic
################ End of nGram_Dict ##############################

#**************** Start of Main *************************************
if __name__ == '__main__':

    #Setting the files names of our 3 training files by language
    train_English = "LangId.train.English.English"
    train_French = "LangId.train.French"
    train_Italian = "LangId.train.Italian.Italian"
    

    #Reading and newline removal to the files
    train_English = readFiles(train_English)
    train_French = readFiles(train_French)
    train_Italian = readFiles(train_Italian)

    #Tokenizing everything
    EnglishToken = word_tokenize(train_English)
    FrenchToken = word_tokenize(train_French)
    ItalianToken = word_tokenize(train_Italian)
    
    #Calling the fuction 3 times for each training file
    Engl_UniDic, Engl_BiDic = nGram_Dict(EnglishToken, train_English)
    Fren_UniDic, Fren_BiDic = nGram_Dict(FrenchToken, train_French)
    Ital_UniDic, Ital_BiDic = nGram_Dict(ItalianToken,train_Italian)

    DB_UniDictionars = {}
    #Adding in our unigram dictionaries
    DB_UniDictionars["English"] = Engl_UniDic
    DB_UniDictionars["French"] = Fren_UniDic
    DB_UniDictionars["Italian"] = Ital_UniDic
    
    #Ez storage for our 3 bigram dictionaries
    DB_BIDictionars = {}
    #Adding in our Bigram dictionaries
    DB_BIDictionars["English"] = Engl_BiDic
    DB_BIDictionars["French"] = Fren_BiDic
    DB_BIDictionars["Italian"] = Ital_BiDic

    #Pickeling the 6 total dictionaries from each language we have done
    DBfile_UniDic = open("DBfile_UniDic.pickle", 'wb')
    DBfile_BiDic = open("DBfile_BiDic.pickle", 'wb')

    pickle.dump(DB_UniDictionars, DBfile_UniDic)
    pickle.dump(DB_BIDictionars, DBfile_BiDic)

  #  loadData() 

    #Closing our created files
    DBfile_UniDic.close()
    DBfile_BiDic.close()
#****************End of Main*************************************





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
        
  #  dbfile_Unigram.close()
   # dbfile_Bigram.close()

   # return db_Unigram, db_Bigram