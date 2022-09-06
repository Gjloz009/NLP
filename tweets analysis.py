'''
vamos a intentar a darle ya solución al problema
que tenemos

'''
# importamos la tabla que tenemos 
from ast import pattern
from pickletools import read_uint1
from queue import Empty
import pandas as pd
import re 

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
tmp_01.value_counts(['lang','truncated'])

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

# vamos por entities_hashtags 
tw_hashtags = tmp_01.entities_hashtags
tw_hashtags.astype('string')
tw_truncated.agg(['shape','count','nunique'])
tw_hashtags.value_counts()
tmp_01.value_counts(['lang','entities_hashtags'])

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
# vamos por el campo entities user mentions
tw_user_mentions = tmp_01.entities_user_mentions
tw_user_mentions.agg(['shape','count','nunique']) #tenemos valores nulos
# son 2885 valores no nulos y 2014 valores unicos 
tw_user_mentions.value_counts()
'''
TOP 5:
nexta_tv          51
olex_scherba      36
PMoelleken        32
YourAnonOne       26
Mediavenir        25

podriamos ver quienes son y cual es la relevancia
dentro del conflicto. Es de investigar las personas
relevantes dentro de este conflicto, cómo lo 
pueden ser el presidente, primer ministro, etc.
'''
# vamos ahora por entitites_urls 
tw_urls = tmp_01.entities_urls
tw_urls.agg(['shape','count','nunique']) #no hay valores nulos
# 736 valores unicos 
tw_urls.value_counts() 
'''
la mayoria no contienen elementos, sería bueno inpeccionar que 
se refiere todos estos urls , si son fotos o que son.
Tambien hay que darle limpieza pues contienen mas valores.
'''

# vamos a entrar con el campo geo 
tw_geo = tmp_01.geo
# son 3602 valores  
tw_geo.count() # son puros valores NaN
'''ESTA COLUMNA ES INSERVIBLE'''

#vamos por la columna coordinate
tw_cord = tmp_01.coordinates
tw_cord.agg(['shape','count','nunique']) #no hay valores nulos
# 736 valores unicos 
tw_cord.value_counts()
tw_cord.sample(5)
'''ESTA COLUMNA NO SIRVE'''

# vamos por la columna retweet count 
tw_rt_cnt = tmp_01.retweet_count
tw_rt_cnt.agg(['shape','count','nunique']) #no hay valores nulos
# 1080 valores unicos 
tw_rt_cnt.value_counts()

'''
La distribución muestra que 
son más los tweets que no tienen relevacia 
son solo tweets únicos, si tuvieramos manera de
ver quien escribión los tweets relevantes
sería un buen guiño.
'''

# vamos por la columna favorite count 
tw_fv_cnt = tmp_01.favorite_count
tw_fv_cnt.agg(['shape','count','nunique']) #no hay valores nulos
# 58 valores unicos 
tw_fv_cnt.value_counts()

'''
De igual manera la distribución es inversa , es decir
son más los tweets sin relevancia
'''


# ahora vamos a ver el campo lang 
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
# vamos con el ultimo campo place 
tw_place = tmp_01.place
tw_place.agg(['shape','count','nunique']) #18 valores no nulos solamente
# 18 valores unicos 
tw_place.value_counts()
'''
Aunque solo tenemos 18 valores no nulos, 
podríamos ver cual es el contenido el numero de 
rt , el numero de fv y trater de ver si existe cierta
relación.
También se necesita hacer limpieza de los valores'''


'''
####################################################


Ahora vamos a crear un dataframe limpio, con el tipo
de valores que consideramos los correctos y con el arreglo
de las columnas que habiamos mencionado
'''

# vamos primero con entities urls 

# vamos con definir nuestro regex 
def x(stringg):
    a = re.findall("'url':\\s'(.*?)',",stringg)
    if len(a) != 0:
        return a[0]
    else:
        return None

# ahora vamos con la otra columna que se tienen que limpiar

type(prueba_3)
def x_2(stringg):

    a = re.findall("'country_code':\\s'(.*?)'",stringg)
    if len(a) != 0:
        return a[0]
    else:
        return None

# ahora eliminamos las columnaas que no sirven y tendriamos nuestro data frame limpio
# que son coordinates y geo 
tmp_02 = tmp_01.drop(columns=['coordinates','geo'])
tmp_02.columns

# aplicamos las funciones creadas
tmp_02['place'] = tmp_02['place'].astype('str')
tmp_02['place'] = tmp_02['place'].apply(x_2)
tmp_02['entities_urls'] = tmp_02['entities_urls'].apply(x)

# guardamos todo en un nuevo dataframe para no estar haciendo este proceso 
path = "D:/jafet/Github/RussoUkrainianWar_Dataset/prueba/"
# tmp_02.to_csv(f'{path}\{"tmp_02_limpio.csv"}')


