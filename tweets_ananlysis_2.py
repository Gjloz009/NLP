'''
dada nuestras referencias nos podría interesar
tener cada columna con un tipo de dato en especifico

Se creo un dashboard de diferentes conteos interesantes utliziando 
power bi, una gran herramienta.
Es tiempo de pasar al análisis de texto que realmente es lo que nos
interesa. Analizar texto.
    
'''

import nltk
import pandas as pd

# tenemos que tomar entonces la columna texto 

path = "D:/jafet/Github/RussoUkrainianWar_Dataset/prueba/"
tmp_02 = pd.read_csv(
    f'{path}\{"tmp_02_limpio.csv"}'
    ,index_col='Unnamed: 0'
    ,dtype={
        'text':'string'
        ,'created_at':'object'
        ,'id':'int64'
        ,'truncated':'bool'
        ,'entities_hashtags':'string'
        ,'entities_user_mentions':'string'
        ,'entities_urls':'string'
        ,'retweet_count':'int64'
        ,'favorite_count':'int64'
        ,'lang':'category'
        ,'place':'category'
        }
    )

# vamos a tomar la columna texto pero en ingles 
texto = tmp_02.text.loc[tmp_02.lang == 'en']

# vamos a normalizarlo 
texto = texto.str.lower()
# parece ser que tenemos muchos RT , entonces veremos cuantos son 
texto.loc[texto.str.startswith('rt')].sample(n=5)
# son 1627 valores 

# me preocupan estos valores , quiero ver si hay valores repetidos 
texto.agg(['count','nunique','shape','is_unique']) #hay como doscientos valores repetidos
# como identificar los valores repetidos 

# logramos identificar los valores repetidos y todos son rt 
texto.loc[texto.duplicated()].str.startswith('rt').all()

# nos quedaremos unicamente con textos no repetidos para que los
# conteos no se vean afectados 
texto = texto.drop_duplicates()
'''
Proceso para utilizar la librería :
    -decidir si viene todo en una sola lista o si metemos tweet
    por tweet
    -checar si el tipo de formato en el que viene 
    nos sirve para tener palabras completas
    -checar el tipo de idioma que viene para ver 
    si nos sirve para obtener palabras completas
    -tokenizar el texto con word_tokenize(),che
    car parametros para hacerlo de la mejor manera 
    posible.
    -lemmantizar palabras
    -tokenizar para separar texto con no texto???
    -creat un objeto NLTK text con nltk.Text()
    -definir palabras y vocabulario.
    -identificar qu econteos vamos a hacer

    
    siento que la forma en que se importo no es la manera correcta
'''
# quitamos whitespaces a los lados 
texto =  texto.str.strip()
texto.sample(n=5)

# hacemos solo un texto grande de nuesto sample 
texto_largo = ' '.join([word for word in texto])

len(texto_largo) #tenemos 222752 

# vamos a probar diferentes formas de tokenizar para quedarnos con
# la mejor 

# tokenizacion base 
tokens_01 = nltk.word_tokenize(texto_largo,language='english')
len(tokens_01) #tenemos 43,038 tokens es una lista

sorted(tokens_01)


'''
como es posible pensar y visualizar , aunque este método
de tokenización es bueno , deja afuera cosas como apostofres
de palabras que estan contraidas, guiones y palabras entrecom
illadas'''

pattern = r'''(?x)     # set flag to allow verbose regexps
    (?:[A-Z]\.)+       # abbreviations, e.g. U.S.A.
  | \w+(?:-\w+)*       # words with optional internal hyphens
  | \$?\d+(?:\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
  | \.\.\.             # ellipsis
  | [][.,;"'?():-_`]   # these are separate tokens; includes ], [
'''
tokens_02 = nltk.regexp_tokenize(texto_largo,pattern)
len(tokens_02) # tenemos 41,941
sorted(tokens_02)[0:200]
sorted(tokens_01)[0:200]

# no me convence, tengo que definir mis propios regex para el probema
'''
que quisiera guardar y que no:
- quisera todo el vocabulario con las palabras completas
    - palabras con apostofre
    - palabras con guion en medio
    - palabras con underscore
    - palabras entrecomilladas
    - no quiero los rt
    - no quiero los @usuario:
      completo ,sería la palabra
      sin el @
    - no quiero los hashtags com
      leto, sería la palabra sin
      el #
    - todo lo que tenga que ver 
      con imagenes tambien volarlo 
      o links también volarlo
    -
    - emoticones 
que mas que mas que mas
'''
texto.sample(n=2)
texto.loc[667]
1+2



tweets = nltk.Text(tokens) #convertimos a una clase nltk
tweets.concordance('war')
tweets.similar('russia')
tweets.dispersion_plot(['war','russia','putin','ukraine'])

sorted(set(tweets))

len(set(tweets)) 
# tenemos 7962 palabras , signos de puntuacion, emojis entre otros cosas 

# lexical richness 0.18499
len(set(tweets))/len(tweets)

# count the number of specific word , podemos intentarlo con todas las palabras
tweets.count('war')

# vamos a ver sus frecuencias de nuestros tokens 
fdist1  = nltk.FreqDist(tweets)

# si notamos los top más frequientes son caracteres que no nos sirven mucho 
fdist1.most_common(n=10)

fdist1.plot(50,cumulative=True)

# vamos a ver como funciona con stop words 
from nltk.corpus import stopwords
stopwords.fileids()
'''
Nos sirve:

english
spanish
french
dutch
'''
stopw = stopwords.words('english')

# sin stopwords tenemos 0.74 por ciento de palabras totales 
len([word for word in tweets if word not in stopw])/len(tweets)

# ahora nos quedaremos con ese vocabulario sin stopwords 
tweets_wstp = [word for word in tweets if word not in stopw]
puntuacion_symbols = ['']
stopw
fdist2 = nltk.FreqDist(tweets_wstp)
fdist2.most_common(n=10)
import string
list(string.punctuation)

# tenemos el 0.71 sin los signos de puntuacion 
len([word for word in tweets_wstp if word not in list(string.punctuation)])/len(tweets_wstp)

tweets_wstp_pnt = [word for word in tweets_wstp if word not in list(string.punctuation) and word not in ['rt','https',"'s"]]

fdist3 = nltk.FreqDist(tweets_wstp_pnt)
type(fdist3.most_common(n=10))
fdist3.plot(100)
sorted(set(tweets_wstp_pnt))
tweets_wstp
# podemos pasar esta lista a power bi para plotear
# y también el vocabulario , los tokens y vocabulario 
type(fdist3)


























































texto.agg(['is_unique','shape']) #1764

texto.head(6)
texto.loc[1700]
import re 
1746-1352 #394
texto.str.startswith('rt').sum() #tenemos 1352 tenemos que limpiar esto
'''
 PASOS AREALIZAR:
 -Limpiar el texto:
    -todos los textos con rt
    -utlizar la librería para tokenizar y todo el resto

'''

texto.loc[texto.str.startswith('rt')].sample(n=5)
prueba = texto.loc[72]
prueba_2 = texto.loc[1895]
re.findall(':.*',prueba_2)
def x(stringg):
    a = stringg.startswith('rt')
    if a == True:
        return re.sub('rt\s@.*:',r'',stringg).strip()
    else:
        return stringg
def x_2(stringg):
    if stringg.startswith('rt')==True:
        a =re.findall(':.*',stringg)
        return a[0]
    else:
        return stringg

texto_2 = texto.apply(x_2)
texto.is_unique

texto_2.is_unique
texto_2.loc[texto_2.duplicated().sum()]
# solo hay un duplicado 
texto_2.loc[1700]
texto.loc[1700]
texto_2 = texto_2.drop_duplicates()
texto_2.is_unique
texto_2.sample(n=5)
texto_2 =texto_2.str.strip()

def x(stringg):
    a = re.findall("'url':\\s'(.*?)',",stringg)
    if len(a) != 0:
        return a[0]
    else:
        return None

# aplicamos nuestra funcion 
texto = texto.apply(x)

# checamos si limpiamos bien 
texto.str.startswith('rt').sum()
# notamos que existen valores con rt 
# notamos que ahora a la hora de hacer limpieza existen valores duplicados 
texto.is_unique

texto.duplicated().sum() # son solo seis valores duplicados

texto.loc[texto.duplicated()]
# 754 1700 1921 2661 3464 checar estos valores
texto.sample(n=5)

import nltk
texto = texto.to_numpy()
len(texto)
texto[0]
type(texto)