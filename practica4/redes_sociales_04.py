import tweepy

# Claves de acceso a la API de Twitter
consumer_key = "CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"

# Autenticación
client = tweepy.Client(
    consumer_key=consumer_key, 
    consumer_secret=consumer_secret,
    access_token=access_token, 
    access_token_secret=access_token_secret
)

# Publicación de un tweet
tweet_text = "¡Hola, Mundo! Este es el primer tweet publicado desde este bot."
response = client.create_tweet(text=tweet_text)
# Imprimimos la URL del tweet publicado
print(f"https://twitter.com/user/status/{response.data['id']}")

# Enviamos una imagen
image_path = "image.jpg"
media_id  = api.media_upload(image_path).media_id_string
tweet_text = "¡Hola, Mundo! Esta imagen ha sido publicada desde este bot.
response = client.create_tweet(text=tweet_text, media_ids=[media_id])
