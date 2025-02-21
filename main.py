import telebot
import random
from bot_logic import random_task  # Импортируем функции из bot_logic
from config import token

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7710659074:AAEPyHOySrX4w_Fz2X6Ne5cFkPeYtylN7cU")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Здраствуйте, Китайская Партия приветствует вас! Походу вы заинтересованны в глобальном потеплении, я помочь вам! Каждый день вы можете запрашивать задания, которые помогут от загрязнения и глобального потепления. Для задания напиши /task, когда выполнишь присылай /done")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Китайская Партия ждёт вас завтра!")


@bot.message_handler(commands=['done'])
def send_bye(message):
    bot.reply_to(message, "Молодец!")

    with open("maxresdefault.jpg", "rb") as photo:  # Укажи путь к своей картинке
        bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['task'])
def random_tasks(message):
    task = random_task()
    bot.reply_to(message, f"Ваше задание на сегодня: {task}")

# @bot.message_handler(content_types=['photo'])
# def handle_docs_photo(message):
#     # Проверяем, есть ли фотографии
#     if not message.photo:
#         return bot.send_message(message.chat.id, "Вы забыли загрузить картинку :(")

#     # Получаем файл и сохраняем его
#     file_info = bot.get_file(message.photo[-1].file_id)
#     file_name = file_info.file_path.split('/')[-1]
    
#     # Загружаем файл и сохраняем
#     downloaded_file = bot.download_file(file_info.file_path)
#     with open(file_name, 'wb') as new_file:
#         new_file.write(downloaded_file)


#         result = get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=file_name)
#         bot.send_message(message.chat.id, result)

# Запускаем бота
bot.polling()