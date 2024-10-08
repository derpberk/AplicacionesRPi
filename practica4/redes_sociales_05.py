from instagrapi import Client

username = 'USERNAME' # El usuario de Instagram
password = "CONTRASEÑA." # La contraseña de Instagram
 
# Creamos una instancia de la clase Client y nos logueamos
cl = Client()
cl.login(username, password)

# Obtenemos el id del usuario
user_id = cl.user_id_from_username(username)
print(user_id)

# Publicamos una foto
mensaje = "Esta es mi primera publicación en Instagram desde un script de Python. #Python #RaspberryPi #ETSI"
cl.photo_upload('./image.jpg')
