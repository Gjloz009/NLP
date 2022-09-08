'''
dada nuestras referencias nos podría interesar
tener cada columna con un tipo de dato en especifico
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

path = "D:/jafet/Github/RussoUkrainianWar_Dataset/prueba/"
tmp_02 = pd.read_csv(
    f'{path}\{"tmp_02_limpio.csv"}'
    ,index_col='Unnamed: 0'
    ,dtype={
        'text':'str'
        ,'created_at':'object'
        ,'id':'int64'
        ,'truncated':'bool'
        ,'entities_hashtags':'str'
        ,'entities_user_mentions':'str'
        ,'entities_urls':'str'
        ,'retweet_count':'int64'
        ,'favorite_count':'int64'
        ,'lang':'category'
        ,'place':'category'
        }
    )
tmp_02.to_csv(f'{path}\{"tmp_02_limpio_2.csv"}')
# creamos la columna a su respectivo formato 
tmp_02['created_at'] = pd.to_datetime(tmp_02['created_at'],utc=True)
tmp_02['created_at'].isna().any() # No tenemos datos missing


dates = tmp_02.created_at
tmp_02.created_at

tmp_02.created_at.value_counts().plot.line()
plt.show()

tmp_02.created_at.agg(['min','max']) # solo tenemos un mes

# vamos a reproducir la figura 1 del paper que son conteos de tweets por día 
cnt_tweets = (
    tmp_02
    .text
    .rename(dates)
)

(
    cnt_tweets
    .resample('D')
    .count()
    .plot
    .line()
)
plt.show()

sns.relplot(
    data = tmp_02,
    kind='line',
    x='created_at',
    y='text',
    hue='lang'
)
plt.show()
# reproducir la figura 3 que son conteos por dias por lenguajes
cnt_lan_tw = (
    tmp_02
    .lang
    .rename(dates)
)
cnt_lan_tw 
(
    cnt_lan_tw
    .resample('D')
    .count()
    .plot
    .pie()
)
plt.show()

(
    tmp_02
    .lang
    .value_counts()[:10]
    .plot
    .pie()
)
plt.show()

# reproducir la figura 5  que son conteos totales de tweets por idioma

tmp_02.lang.value_counts()[:10]

(
    tmp_02
    .where(tmp_02.isin(top10))
    .value_counts()
    .plot.barh()
)
plt.show()

tmp_02.where(tmp_02.isin(top10))


'''
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
texto.loc[3597]
# me preocupan estos valores , quiero ver si hay valores repetidos 
texto.agg(['count','nunique','shape']) #hay como doscientos valores repetidos
# como identificar los valores repetidos 