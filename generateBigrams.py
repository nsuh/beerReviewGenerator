import nltk
import pandas as pd
from itertools import chain
from nltk.probability import ConditionalFreqDist
from nltk.corpus import brown
from nltk.util import bigrams
from nltk.probability import ConditionalFreqDist
from itertools import chain

f = open('beerReviews.txt')
raw = f.read()
tokens = nltk.word_tokenize(raw)

#Create your bigrams
bigrams = nltk.bigrams(tokens)
#print bigrams
#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bigrams)
fd = fdist
#30 most common bigrams
fdist.most_common(30)

countsTable = np.matrix(([[0,185,0,2,0],[0,2,184,24,0],[0,0,1,10,0],[0,0,0,0,23],[0,1,0,0,0]]))
indexNames = ['Pours', 'a', 'nice', 'golden', 'color']
colNames = ['Pours', 'a', 'nice', 'golden', 'color']
countsTable = pd.DataFrame(A, index=indexNames, columns=colNames)
probTable = countsTable.copy() #deep copy
#divide over unigram counts to generate probabilities
probTable.iloc[0,:] = probTable.iloc[0,:]/297
probTable.iloc[1,:] = probTable.iloc[1,:]/37222
probTable.iloc[2,:] = probTable.iloc[2,:]/438
probTable.iloc[3,:] = probTable.iloc[3,:]/191
probTable.iloc[4,:] = probTable.iloc[4,:]/399