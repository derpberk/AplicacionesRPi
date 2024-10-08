from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import cv2

# Token del bot, generado mediante BotFather
TOKEN = "EL_TOKEN_DEL_BOT"

mensaje_ayuda = "Hola. Soy un bot que convierte \
    las imágenes a blanco y negro."

# Definimos las funciones manejadoras de los comandos

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Función que se ejecuta cuando se envía el comando /start """
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Función que se ejecuta cuando se envía el comando /help """
    await update.message.reply_text(mensaje_ayuda)


async def func_texto_recibido(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """ Función que se ejecuta cuando se envía un mensaje de texto """
    # Obtenemos el mensaje del usuario
    mensaje_de_respuesta = "He recibido el siguiente mensaje: " + update.message.text
    # Respondemos al mensaje
    await update.message.reply_text(mensaje_de_respuesta)
    
async def get_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("He recibido una foto!")
    # Obtenemos el archivo.
    new_file = await context.bot.get_file(update.message.photo[-1].file_id)
    # Descargamos el archivo
    await new_file.download_to_drive('./image.jpg')
    # Leemos la imagen y la pasamos a blanco y negro
    image = cv2.imread('image.jpg') 
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Guardamos la  nueva imagen
    cv2.imwrite('image_gray.jpg', gray_image)
    # La enviamos 
    await update.message.reply_photo(photo=open('image_gray.jpg', 'rb'))
    
def main() -> None:
    """ Función principal que inicializa el bot """
    # Creamos la aplicación con el TOKEN del bot #
    application = Application.builder().token(TOKEN).build()
    
    # Asociamos los comandos a las funciones manejadoras
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    # Asociamos la función manejadora de mensajes de texto que no son comandos
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, func_texto_recibido))
    application.add_handler(MessageHandler(filters.PHOTO, get_image))

    # Iniciamos el bot y lo dejamos correr hasta que se presione Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()