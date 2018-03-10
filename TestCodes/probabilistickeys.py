from nltk import word_tokenize, pos_tag
from nltk.corpus import state_union, stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import PunktSentenceTokenizer as punk, sent_tokenize
from collections import defaultdict as dd

file_name = "hash1.txt"  #FILENAME with .txt

def readfile(file): #Reads contents of the input file
    try:
        with open(file,"r") as f:
            sample_text=f.read()
        return sample_text
    except:
        print("Input File could not be found!")
    raise SyntaxError(file)     #If the file specified could not be found

def filtertoken(tokened): #input sentence-tokenized list
    keywords=[]
    try:
        for i in tokened:
            words = word_tokenize(i)    #word tokenise each sentence
            tagged = pos_tag(words)     #tag for each word
            #print(tagged)
            for j in tagged:
                if j[1] in keyparam and len(j[0])>1:    #checking tag and removing single charachters
                    #print(j,sep=' ')
                    keywords.append(j[0])
    except Exception as e:
        print(str(e))
        keywords=[]
    return keywords

def counts(toklist):    #Counts the occurence of each word
    di = dd(int)
    for i in toklist:
        di[i.lower()] += 1
    return di

threshold = 6   #Minimum number of occurences required to be selected
keyparam=['CD','FW','NN','NNP','NNS','NP','NPS','VB','VBD','VBG','VBN','VBP',
                    'VBZ','VH','VHD','VHG','VHN','VHP','VHZ','VV','VVD','VVG','VVN',
                    'VVP','VVZ','WP','WP$','WRB'] #POS tags which are allowed
stop_words=set(stopwords.words('english')) #Set of stop words
stemmer = SnowballStemmer("english")        #Stemmer

sample_text=readfile(file_name)
tokenized = filtertoken(word_tokenize(sample_text)) #Filters the tokens based on keyparam

filtered = [w for w in tokenized if not w in stop_words] #Removes stop words
z = counts(filtered)
print("Unstemmed:")
print([w for w in z if z[w]>threshold])
z = counts(map(stemmer.stem,filtered))      #Stems the keywords
print("After stemming:")
print([w for w in z if z[w]>threshold])
