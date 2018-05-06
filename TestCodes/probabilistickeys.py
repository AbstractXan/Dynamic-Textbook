import nltk #word_tokenize, pos_tag
from nltk.corpus import state_union, stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import PunktSentenceTokenizer as punk, sent_tokenize
from collections import defaultdict as dd


def readfile(file): #Reads contents of the input file
    try:
        with open(file,"r") as f:
            sample_text=f.read()
        return sample_text
    except:
        print("Input File could not be found!")
    raise SyntaxError(file)     #If the file specified could not be found

class KeyFilter:
    
    keyparam=['CD','FW','NN','NNP','NNS','NP','NPS','VB','VBD','VBG','VBN','VBP',
                    'VBZ','VH','VHD','VHG','VHN','VHP','VHZ','VV','VVD','VVG','VVN',
                    'VVP','VVZ','WP','WP$','WRB']    #POS tags which are allowed

    def __init__(self, thresh = 6):
        self.stemmer = SnowballStemmer("english")       #Stemmer
        self.threshold = thresh     #Minimum number of occurences required to be selected

    def tokenize(self,fullstring):      #Takes a string as input and tokenizes them with pos tags
        tokenized = KeyFilter.filtertoken(nltk.word_tokenize(sample_text)) #Filters the tokens based on keyparam
        return tokenized

    @staticmethod
    def filtertoken(tokened): #input sentence-tokenized list
        keywords=[]
        try:
            for i in tokened:
                words = nltk.word_tokenize(i)    #word tokenise each sentence
                tagged = nltk.pos_tag(words)     #tag for each word
                #print(tagged)
                for j in tagged:
                    if j[1] in KeyFilter.keyparam and len(j[0])>1:    #Checking tag and removing single charachters
                        #print(j,sep=' ')
                        keywords.append(j[0])
        except Exception as e:
            print(str(e))
            keywords=[]
        return keywords

    def stopfilter(tokenized):    #Takes a list of words and removes stopwords
        stop_words=set(stopwords.words('english')) #Set of stop words
        filtered = [w for w in tokenized if not w in stop_words] #Removes stop words
        return filtered

    @staticmethod
    def counts(toklist):    #Counts the occurence of each word
        di = dd(int)
        for i in toklist:
            di[i.lower()] += 1
        return di

    def unstemmedKeys(self,string):
        words = KeyFilter.stopfilter(self.tokenize(string))
        count = KeyFilter.counts(words)
        return [w for w in count if count[w]>self.threshold]

    def stemmedKeys(self,string):
        words = KeyFilter.stopfilter(self.tokenize(string))
        count = KeyFilter.counts(map(self.stemmer.stem,words))
        return [w for w in count if count[w]>self.threshold]

if __name__=="__main__":
    
    file_name = "hash1.txt"  #FILENAME with .txt
    sample_text=readfile(file_name)
    filt = KeyFilter(6)
    print("Unstemmed:")
    print(filt.unstemmedKeys(sample_text))
    print("After stemming:")
    print(filt.stemmedKeys(sample_text))
