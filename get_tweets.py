'''
Código para la creación de una tabla con tweets extraidos por
los ID recolectados por el archivo de investigación 
https://www.researchgate.net/publication/360062365_Twitter_Dataset_on_the_Russo-Ukrainian_War.


Consideraaciones y areas de oportunidad:
    -Algunos tweets ya no existen (última corrida 25/08/2022).
    -hacer el proceso de construccion de 
    diccionario de tweets con librerías donde buscamos la optimización 
    de tiempos.
    -mejorar la recolección de tweets por medio de la api,
    es decir, que la recolección no sea un proceso uno por uno.
    -solo se considera una sola corrida, si existen archivos de
    salida dentro de la misma carpeta serán considerados en procesos
    donde no se requieren.


Tiempo de ejecución aproximada:
5H:45M:00S
'''


'''
********MODULOS********
'''
from html import entities
from functools import partial 
import pandas as pd
import tweepy
import random
import os



'''
********FUNCIONES******
'''
# definimos una funcion que extraemos los twees desde el tweet_id
def get_json(file):
    a = list()
    print(len(file))
    for id in file:
        id = id.rstrip()
        try:
            prueba = api.get_status(id,
            include_ext_alt_text = 'false')
            json_file = prueba._json
            refined_tweet = {
                'text' : json_file['text'],
                'created_at' : json_file['created_at'],
                'id' : json_file['id'],
                'truncated' : json_file['truncated'],
                'entities_hashtags' : json_file['entities']['hashtags'],
                'entities_user_mentions' : json_file['entities']['user_mentions'],
                'entities_urls' : json_file['entities']['urls'],
                'geo' : json_file['geo'],
                'coordinates' : json_file['coordinates'],
                'retweet_count' : json_file['retweet_count'],
                'favorite_count' : json_file['favorite_count'],
                'lang' : json_file['lang'],
                'place' : json_file['place']
            }
            a.append(refined_tweet)
        except:
            continue
    return a


#funcion que haremos para abrir multiples archivos 
def union(path):
    import os

    # cambiamos de directorio
    os.chdir(path)

    variable = list()
    def read_txt_file(file_path):
        with open(file_path,'r') as f:
            for line in f:
                # line = line.rstrip()
                variable.append(line)

    for file in  os.listdir():
        print(len(variable))
        if file.endswith('.txt'):
            file_path = f'{path}\{file}'
            read_txt_file(file_path)
    return variable

# funcion para escrbibr archivos txt de uso para filtar los id que sirven 
def write_fast(valor,nombre):
    
    with open(f'{path_2}\{nombre}','a') as f:
        try:
            id = valor.rstrip()
            var = api.get_status(id,include_ext_alt_text = 'false')
            f.write(valor)
        except:
            # f.write('no esntra\n')
            pass

# funcion que limpia las columnas con multiples entradas 
def limpieza(lista):
    for i in range(len(lista)):

        # lista[i]['display_text_range'] = lista[i]['display_text_range'][1]    

        if len(lista[i]['entities_hashtags']) > 0:
                lista[i]['entities_hashtags'] = lista[i]['entities_hashtags'][0]['text']
        else:
             lista[i]['entities_hashtags'] = None

        if len(lista[i]['entities_user_mentions']) > 0:
                lista[i]['entities_user_mentions'] = lista[i]['entities_user_mentions'][0]['screen_name']
        else:
            lista[i]['entities_user_mentions'] = None

        if len(lista[i]['entities_urls']) > 0:
                lista[i]['entities_urls'] = lista[i]['entities_urls'][0]['url']
        else:
            lista[i]['entities_urls'] = None
'''
********END FUNCIONES********
'''



'''
********CODIGO********
'''
consumer_key = "contraseña1"
consumer_secret = 'contrseña2'
accces_key = 'contraseña3'
acces_secret = 'contraseña4'


# autenticación de la api
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(accces_key,acces_secret)

# creando un objeto api
api = tweepy.API(auth)

# si esto ya salío bien ya tenemos acceso a los dferentes twwet



# obtenemos todos los tweets_id de los aarchivos de texto que se tiene 
path = 'D:/jafet/Github/RussoUkrainianWar_Dataset/2022-02'
lines_02=union(path)

path = 'D:/jafet/Github/RussoUkrainianWar_Dataset/2022-03'
lines_03=union(path)

path = 'D:/jafet/Github/RussoUkrainianWar_Dataset/2022-04'
lines_04=union(path)

path = 'D:/jafet/Github/RussoUkrainianWar_Dataset/2022-05'
lines_05=union(path)

path = 'D:/jafet/Github/RussoUkrainianWar_Dataset/2022-06'
lines_06=union(path)

path = 'D:/jafet/Github/RussoUkrainianWar_Dataset/2022-07'
lines_07=union(path)

path = 'D:/jafet/Github/RussoUkrainianWar_Dataset/2022-08'
lines_08=union(path)


# creamos samples del .5 por ciento del total
lines_02_sample = random.sample(lines_02,int(len(lines_02)*.0005))
lines_03_sample = random.sample(lines_02,int(len(lines_03)*.0005))
lines_04_sample = random.sample(lines_02,int(len(lines_04)*.0005))
lines_05_sample = random.sample(lines_02,int(len(lines_05)*.0005))
lines_06_sample = random.sample(lines_02,int(len(lines_06)*.0005))
lines_07_sample = random.sample(lines_02,int(len(lines_07)*.0005))
lines_08_sample = random.sample(lines_02,int(len(lines_08)*.0005))
len(lines_08_sample)

# tenemos que darle otro aproach aprovechando la vectorrizacion
# por tanto lo haremos con la funcion map para listas 

path_2 = 'D:/jafet/Github/RussoUkrainianWar_Dataset/prueba'

vemos = list(map(partial(write_fast,nombre='lista_02.txt'),lines_02_sample))
vemos
vemos = list(map(partial(write_fast,nombre='lista_03.txt'),lines_03_sample))
vemos
vemos = list(map(partial(write_fast,nombre='lista_04.txt'),lines_04_sample))
vemos
vemos = list(map(partial(write_fast,nombre='lista_05.txt'),lines_05_sample))
vemos
vemos = list(map(partial(write_fast,nombre='lista_06.txt'),lines_06_sample))
vemos
vemos = list(map(partial(write_fast,nombre='lista_07.txt'),lines_07_sample))
vemos
vemos = list(map(partial(write_fast,nombre='lista_08.txt'),lines_08_sample))
vemos

'''
tenemos entonces samples de cada mes ,estos samples son el .00005 del total del nummero
de tweets de cada mes , ahora dependde de cuantos tweets quedaron que si contiene
información. Obtendremos la información y haremos un análisis.

las longitudes son:
lista_02.txt
3158
lista_03.txt
8219
lista_04.txt
1132
lista_05.txt
869
lista_06.txt
1169
lista_07.txt
365
lista_08.txt
332
'''

# con esto en mente, podemos extraer la información de la api 
# para eso juntamos todos los samples 
# tenemos entonces 15244 id_tweets de nuestros meses 

tmp_01 = union(path_2)
len(tmp_01)

# guardamos un txt con el junte de tdo 
nombre = 'tmp_01.txt'
with open(f'{path_2}\{nombre}','w') as f:
    f.writelines(tmp_01)

# procedemos a entonces extraer los valores
tmp_02 = get_json(tmp_01)

len(tmp_02)


# limpiamos un poco los valores de hashtag y user mention
limpieza(tmp_02)

# transformando en df 

df = pd.DataFrame(tmp_02)
df.head(2)
df.to_csv(f'{path_2}\{"tmp_02_pr2.csv"}')
'''
********END CODIGO********
'''