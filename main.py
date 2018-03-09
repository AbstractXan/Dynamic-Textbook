from nltk import word_tokenize, pos_tag
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer as punk
from api import *

file_name = " FILENAME.txt "  #FILENAME with .txt
htmlname  = " HTMLNAME "      #Target HTML name without .html

################# Functions #####################
def readfile(file):
    try:
        with open(file,"r") as f:
            sample_text=f.read()
        
    except:
        print("Input File could not be found!")
        sample_text="File"          #If the file specified could not be found
    return sample_text

def printtokenlist(tokened): #input sentence-tokenized list
    keywords=[]
    try:
        for i in tokened:
            words = word_tokenize(i)    #word tokenise each sentence
            tagged = pos_tag(words)     #tag for each word
            #print(tagged)
            for j in tagged:
                if j[1] in keyparam and len(j[0])>1 and j[0] not in keywords:    #checking tag and removing single characters and soring in a list
                    #print(j,sep=' ')
                    keywords.append(j[0])
    except Exception as e:
        print(str(e))
        keywords=[]
    return keywords

def printtoken(tokened): #input sentence-tokenized list
    keywords=set()
    try:
        for i in tokened:
            words = word_tokenize(i)    #word tokenise each sentence
            tagged = pos_tag(words)     #tag for each word
            #print(tagged)
            for j in tagged:
                if j[1] in keyparam and len(j[0])>1:    #checking tag and removing single charachters
                    #print(j,sep=' ')
                    keywords.add(j[0])
    except Exception as e:
        print(str(e))
        keywords=set()
    return keywords

#'IN' deleted for crime to add 'at'
#keyparam=['CD','FW','NN','NNP','NNS','NP','NPS','VB','VBD','VBG','VBN','VBP','VBZ','VH','VHD','VHG','VHN','VHP','VHZ','VV','VVD','VVG','VVN','VVP','VVZ','WP','WP$','WRB']
keyparam=["NNP"]
"""
#Check 'posid.txt' to select key param for reference to types of keywords to include eg. nouns,verbs
"""

#################### MAIN #####################

sample_text=readfile(file_name)
cust=punk()
print("Tokenizing...")
tokenized = cust.tokenize(sample_text)
print("Selecting keys...")
keys=printtokenlist(tokenized) #keys=filtered keywords in order
print(keys)
hyperlo=CreateHTML(htmlname)   #hyperlo: Object for file handling and passing query
print("Fetching request...")
for i in keys:
    print("Fetching "+i+"...")
    hyperlo.addquestion(i)          #fetching q and a for each keyword
hyperlo.endquestion()               #closing html document
