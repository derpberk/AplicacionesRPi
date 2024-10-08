import smtplib

correo = "alumno1@gmail.com"
password = "CONTRASEÑA_APLICACION_GOOGLE"

# Nos conectamos al servidor de correo
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(correo, password)

# Definimos los datos del correo
correo_destino = "mi_cuenta_personal@gmail.com"
mensaje = "¡Hola! Este correo ha sido enviado desde Python."
asunto = "Correo de prueba"

# Creamos el mensaje
msg = f"Subject: {asunto}\n\n{mensaje}"

# Enviamos el correo
server.sendmail(correo, correo_destino, msg)

