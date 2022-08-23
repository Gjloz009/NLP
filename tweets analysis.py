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
consumer_key = "intorduce tus llaves:que cambia"
consumer_secret = 'introduce la otra lllavveaaaaa'
accces_key = 'tres llaves'
acces_secret = 'ultima llave'

# autenticación de la api
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(accces_key,acces_secret)

# creando un objeto api
api = tweepy.API(auth)

# si esto ya salío bien ya tenemos acceso a los dferentes twwets

# Tomamos entonces a un usuario controversial "Ricardo Salinas Pliego"
new_tweets = tweepy.Cursor(api.user_timeline,
screen_name="tunguz",
tweet_mode='extended',
exclude_replies='true',
include_rts='false').items(10)

lista  = []
for tweet in new_tweets:

    text = tweet._json["full_text"]
    
    refined_tweet = {
        'text' : text,
        'created_at' : tweet.created_at,
        'id' : tweet.id,
        'display_text_range' : tweet.display_text_range,
        #'entities' : tweet.entities,
        'entities_hashtags' : tweet.entities['hashtags'],
        'entities_user_mentions' : tweet.entities['user_mentions'],
        #'in_reply_to_status_id' : tweet.in_reply_to_status_id, 
        #'in_reply_to_user_id' : tweet.in_reply_to_user_id,
        #'in_reply_to_screen_name' :tweet.in_reply_to_screen_name,
        'geo' : tweet.geo,
        'coordinates' : tweet.coordinates,
        #'place' : tweet.place,
        #'contributors' : tweet.contributors,
        #'is_quote_status' : tweet.is_quote_status,
        'retweet_count' : tweet.retweet_count,
        'favorite_count' : tweet.favorite_count,
        #'favorited' : tweet.favorited,
        #'retweeted' : tweet.retweeted,
        #'lang' : tweet.lang
    }

    lista.append(refined_tweet)
    
# limpiamos un poco los valores de hashtag y user mention
for i in range(len(lista)):

    lista[i]['display_text_range'] = lista[i]['display_text_range'][1]    
    
    if len(lista[i]['entities_hashtags']) > 0:
            lista[i]['entities_hashtags'] = lista[i]['entities_hashtags'][0]['text']
    else:
         lista[i]['entities_hashtags'] = None

    if len(lista[i]['entities_user_mentions']) > 0:
            lista[i]['entities_user_mentions'] = lista[i]['entities_user_mentions'][0]['screen_name']
    else:
        lista[i]['entities_user_mentions'] = None