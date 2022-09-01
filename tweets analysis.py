'''
vamos a intentar a darle ya solución al problema
que tenemos

'''
# importamos la tabla que tenemos 
import pandas as pd

tmp_01 = pd.read_csv(
    "D:/jafet/Github/RussoUkrainianWar_Dataset/prueba/tmp_02_pr2.csv"
    , index_col= 'Unnamed: 0'
    )

# vamos a revisar las columnas poco a poco 
tmp_01.head(2)
# la columna texto es muy amplia no nos deja visualizar 
tmp_01.columns
'''
text -> object 
created_at -> object, fechas pero en texto
id -> int64
truncated -> bool
entities_hashtags -> object
entities_user_mentions -> object
entities_urls -> object
geo -> float64
coordinates -> float64
retweet_count -> int64
favorite_count -> int64 
lang -> object
place -> object
'''

# vamos a entrar al campo id 

tw_id = tmp_01.id
tw_id.shape # son 3602
tw_id.count() # no hay valores nulls
tw_id.nunique() # todos son valores diferentes

# vamos por es campo truncated 
tw_truncated = tmp_01.truncated
tw_truncated.agg(['count','nunique']) #no hay valores nulos, 
#son dos categorias
tw_truncated.value_counts()
'''
False    3207
True      395

tenemos entonces tweests truncados,podemos entonces
ver de que idioma son y ver en que afecta

lang  truncated
en    False        1801
en    True          238
fr    False         250
de    False         133
es    False         127

entonces si tenemos tweets truncados de nuestro
idioma principal
'''
tmp_01.value_counts(['lang','truncated'])

# vamos por entities_hashtags 
tw_hashtags = tmp_01.entities_hashtags
tw_hashtags.astype('string')
tw_truncated.agg(['shape','count','nunique'])
tw_hashtags.value_counts()

'''
TOP 5:
Ukraine             570
StandWithUkraine    120
Russia               91
Putin                75
WWIII                68

podemos ver como se distribuyen por idioma

lang  entities_hashtags  
en    Ukraine                388
      Russia                  77
      StandWithUkraine        71
fr    Ukraine                 56
en    Anonymous               41

es de notar cómo se distribuyen.
'''

tmp_01.value_counts(['lang','entities_hashtags'])

# ahora vamos a ver cuantos tweets por pais tenemos 

tw_lang = tmp_01.lang
tw_lang.shape #tenemos 3602 valores totales
tw_lang.count() #tenemos 3602 valores no nulos
tw_lang.nunique() #tenemos 48 categorías

# contamos entonces cuanto tweets tenemos por país 
tw_lang.value_counts()

'''
TOP 5:
en     2039
fr      264
de      158
es      141
th      109
qme     102

son idiomas bastantes comunes creo que se 
pueden trabajar bajo el análisis que esta-
mos proponiendo. Por primera instancia tra-
bajaremos con ingles.
'''

# vamos a entrar con el campo geo 

tw_geo = tmp_01.geo
# son 3602 valores  
tw_geo.count() # son puros valores NaN
'''ESTA COLUMNA ES INSERVIBLE'''


