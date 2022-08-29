'''
notas de libro nlp with python
'''

# chapter 1 

import imp
from msilib.schema import Condition
from random import sample
from socket import AI_NUMERICHOST
from sre_parse import CATEGORIES
from tkinter import wantobjects
import nltk

# abre wizard para descargar las cosas de la librería 
nltk.download()

from nltk.book import *
# los libros estan puestos como textn con n los enteros
# text1

text1.concordance('whale')

text1.similar('whale')

text4.dispersion_plot(['citizens','democracy','freedom'])
sorted(set(text3))

len(set(text9))/len(text3)
text4.count('a')
100*text4.count('a')/len(text3)

fdist1 = FreqDist(text1)
fdist1.plot(50,cumulative=True,percents=True)
fdist1.hapaxes()


v = set(text1)
long_words = [w for w in v if len(v) > 15]
long_words

fdist5 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)

list(bigrams(['more','is','said']))

text4.collocations( )

text2.dispersion_plot(['Elinor','Marianne','Edward'])

len(sorted(set(w.lower() for w in text1)))
len(sorted(w.lower() for w in set(text1)))

a =sorted(set(w.lower() for w in text1))
b =sorted(w.lower() for w in set(text1))
[x for x in b if  x not in a]

len(set( text5))
four_letter=[x for x in text5 if len(x) == 4]

four_dist=FreqDist(four_letter)

four_dist.most_common(5)
len(four_dist.hapaxes())
four_dist.plot(cumulative=False)

# capituloo 2 
nltk.corpus.gutenberg.fileids()

emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
len(emma)
emma.concordance('surprize')

from nltk.corpus import gutenberg
gutenberg.fileids()

for fileid  in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(num_chars/num_words),round(num_words/num_sents),round(num_words/num_vocab),fileid)

from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid,webtext.raw(fileid)[:65],'...')

from nltk.corpus import brown
news_text = brown.words(categories = 'news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can','could','may','might','must','will']
for m in modals:
    print(m + ':',fdist[m],end = ' ')


from nltk.corpus import brown

prueba =nltk.ConditionalFreqDist(
    (genre,words)
    for genre in ['news','romance']
    for words in brown.words(categories=genre)
)
prueba.tabulate(samples = ['can','could'])
len(prueba)
days = ['Monday','Tuesday']
prueba.plot(cumulative=True)
len(brown.words())

 