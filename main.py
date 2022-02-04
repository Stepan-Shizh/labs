import telebot
from telebot import types

token = "5279481604:AAFxIOa5iyWJ0ItT9c63ejmr9WyjdbmNy-k"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/information", "/help", "/registration")
    bot.send_message(message.chat.id, "Привет! Что хочешь спросить?", reply_markup=keyboard)
@bot.message_handler(commands=['registration'])
def get_name(message): #получаем фамилию
    bot.send_message(message.from_user.id, "Имя")
    global name
    name=message.text
    bot.register_next_step_handler(message,get_surname)
def get_surname(message):
    bot.send_message(message.from_user.id,"Фамилия")
    global surname
    surname=message.text
    bot.register_next_step_handler(message,get_age)
def get_age(message):
    bot.send_message(message.from_user.id,"Возраст")
    global age
    age=message.text
    try:
        age=int(message.text) #проверяем, что возраст введен корректно
    except Exception:
        bot.send_message(message.from_user.id, "Введите цифрами, пожалуйста!")
    bot.send_message(message.from_user.id,"Тебе "+str(age)+" лет, тебя зовут "+name+" "+surname+"?")
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, "Я умею...")
@bot.message_handler(commands=['information'])
def start_message(message):
    bot.send_message(message.chat.id, "Бот разработан студентом Чижом Степаном Анатольевичем из группы БОС1901. Предмет: Информатика")

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower()=="сколько мне лет?":
        if age==0:
            f=2
        bot.send_message(message.chat.id,"Тебе "+str(age)+" лет")
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower()=="3":
        bot.send_message(message.chat.id,"fgfgf")

bot.polling(none_stop=True,interval=2)