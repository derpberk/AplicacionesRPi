from instagrapi import Client

username = 'USERNAME' # El usuario de Instagram
password = "CONTRASEÑA." # La contraseña de Instagram
usuario_instagram = 'instagram name' # El usuario de Instagram al que queremos enviar el mensaje

cl = Client()
cl.login(USERNAME, PASSWORD)
send_to = cl.user_id_from_username(username="usuario_instagram")

cl.direct_send(text="Message", user_ids=[send_to])