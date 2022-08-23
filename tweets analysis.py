# este va a ser nuestro nuevo proyecto

'''
cosas necesarias para el proyecto

Librerías:
-tweepy
-pandas
-nlptk

necesario tener registro en la api de twiter para poder ddescargar los proyectos
'''

import tweepy
# Agregamos las llaves necesarias 
# nunca dejar estas llaves publicas
consumer_key = "intorduce tus llaves"
consumer_secret = 'introduce la otra lllavve'
accces_key = 'tres llaves'
acces_secret = 'ultima llave'

# autenticación de la api
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(accces_key,acces_secret)

# creando un objeto api
api = tweepy.API(auth)

# si esto ya salío bien ya tenemos acceso a los dferentes twwets
