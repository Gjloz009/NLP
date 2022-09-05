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

# ejercico del capitulo dos 
from nltk.corpus import gutenberg

gutenberg.fileids()
gutenberg.categories()
# gutenberg.raw()
len(gutenberg.words('austen-persuasion.txt'))
import nltk
from nltk.corpus import state_union

for fileid in state_union.fileids():
    prueba = nltk.FreqDist(state_union.words(fileid))
    fileid
    prueba['men']
    prueba['women']
    prueba['people']
    
fileid[:4]
prueba = nltk.ConditionalFreqDist(
    (target,fileid[:4])
    for fileid in state_union.fileids()
    for w in state_union.words(fileid)
    for target in ['men','women','people']
    if w.lower() == target
)
prueba.plot()
prueba.conditions()
prueba['men']
prueba['women']
prueba['people']

from nltk.corpus import names
names.fileids()
conditional = nltk.ConditionalFreqDist(
    (fileid,word[0])
    for fileid in names.fileids()
    for word in names.words(fileid)
)
conditional.plot()
conditional.conditions()
conditional['male']
conditional['female']

from nltk.corpus import brown

brown.words()
[palabra for palabra in brown.words() if  len(palabra)==3]
palabra=nltk.FreqDist(brown.words())
palabra.values()

for key in palabra.keys():
    if palabra[key] >20:
        print(palabra[key])

from nltk.book import text1

def zipf(texto):
    b = list()
    freq_texto = nltk.FreqDist(texto)
    a = freq_texto.most_common(200)
    for i in range(len(a)):
        b.append((a[i][0],a[i][1],i))
    return b
aver = zipf(text1)
aver[0][2]

import matplotlib.pyplot as plt
x = [tup[0] for tup in aver]
y = [tup[1] for tup in aver]
y_2 = [tup[2] for tup in aver]

plt.plot(x,y)
plt.plot(x,y_2)
plt.show()
freq_texto = nltk.FreqDist(text1)
a = freq_texto.most_common()
a[:3] 
x[:3]
y[:3]

import nltk, re, pprint
from nltk import word_tokenize
from urllib import request, response

url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw =  response.read().decode('utf8')
type(raw)
len(raw)

tokens = word_tokenize(raw)
type(tokens)
tokens[:5]

text = nltk.Text(tokens)
type(text)
text[1024:1062]
text.collocations()

import re
import nltk
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
[w for w in wordlist if re.search('ed$',w)]

