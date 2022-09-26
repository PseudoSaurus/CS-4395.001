#Set ups for NLTK  
from asyncio.windows_events import NULL
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
#from textblob import TextBlob

def tokenProcess(self):

    #Opening and reading the file
    with open(self) as csvfile:
        content = csvfile.read()

    #tokenizing and lowercasing all the elements
    tokens = word_tokenize(content)
    tokens = [t.lower() for t in tokens]

    return tokens
#End of tokenProcess(self)

def calcula_LexDiv(self):
    #Here is the lexical diversity w/ punctuations and stopwords
    
    #size of self, unique elements
    uniqueTok = len(set(self))

    #size of self
    realLenght = len(self)

    #showing results and LexDiv
    print("\nThis the number of elements your file:", realLenght)
    print("The number of unique element from your file:", uniqueTok)
    # lexical diversity
    print("Lexical diversity: %.2f" % (uniqueTok/ realLenght))

    #Here is the lexical diversity w/out punctuations and stopwords
    print("\n\nNow lets seee the different of lexical diversity when we remove punctuation and stopwords")

    # get rid of punctuation and stopwords
    VIPwords = [t for t in self if t.isalpha() and
           t not in stopwords.words('english')]    

    #size of self, unique elements
    uniqueTok = len(set(VIPwords))

    #size of self
    realLenght = len(VIPwords)

    #showing results and LexDiv
    print("This the number of elements your file:", realLenght)
    print("The number of unique element from your file:", uniqueTok)
    # lexical diversity
    print("Lexical diversity: %.2f" % (uniqueTok/ realLenght))


    return VIPwords
#End of calcula_LexDiv(self):


def Deep_tokenProcess(self):

    #Setting up WordLemman
    WNL = WordNetLemmatizer()

    #Getting only string >5
    largeTokens = [ tok for tok in self if len(tok) > 5 ]
    
    #Lemmantize our token and creating a list of unique lemmans
    tokenLemman = [ WNL.lemmatize(tok) for  tok in largeTokens ]
    tokenLemman_unique = list(set( tokenLemman ) )

    #Getting the tags from our token list
    unique_tags = nltk.pos_tag(tokenLemman_unique)
    print("\n\nHere are the 1st 20 elements from the unique lemman:\n", unique_tags[:20])

    LemmasNouns =[] 
    #Seperating the Nouns from the rest
    for index in range(len(unique_tags)):

        if unique_tags[index][1].startswith('N'):
            LemmasNouns.append(unique_tags[index])
    #LemmasNouns = unique_tags.noun_phrases

    #Printing the length of tokens vs length of nouns
    print("\nI have found {} words that are longer than 5 letters.".format(len(largeTokens)))
    print("I have also found {} unique nouns that are longer than 5 letters.".format(len(LemmasNouns)))

    #showing the first 10 elements from each list
    print("\n\nHere are 10 elements from the regular list, with words having more than 5 letters:\n", largeTokens[:10])
    print("\nHere are 10 elements from the noun list, with words having more than 5 letters:\n", LemmasNouns[:10])

 # non-unique Tokens >5     Noun tokens
    return largeTokens, LemmasNouns    
