import smtplib
from email.message import EmailMessage

correo = "alumno1@gmail.com"
password = "CONTRASEÑA_APLICACION_GOOGLE"

# Nos conectamos al servidor de correo
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(correo, password)

# Definimos los datos del correo
correo_destino = "mi_cuenta_personal@gmail.com"
mensaje = "¡Hola! Este correo ha sido enviado desde Python \
    y contiene un archivo adjunto."
asunto = "Correo de prueba con adjunto"

msg = EmailMessage()
msg['Subject'] = asunto
msg['From'] = correo
msg['To'] = correo_destino
msg.set_content(mensaje)

# Añadimos el archivo adjunto
with open('archivo_adjunto.txt', 'rb') as f:
    file_data = f.read()

msg.add_attachment(file_data, filename='archivo_adjunto.txt')

# Enviamos el correo
server.send_message(msg)


