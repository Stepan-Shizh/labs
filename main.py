import telebot
from telebot import types

token = "5279481604:AAFxIOa5iyWJ0ItT9c63ejmr9WyjdbmNy-k"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/information","/help","/registration")
    bot.send_message(message.chat.id, "Здравствуйте!", reply_markup=keyboard)

name=""
surname=""
age=0
@bot.message_handler(commands=['delete_user'])
def start(message):
    global name,surname,age
    name=""
    surname=""
    age=0
    bot.send_message(message.chat.id, "Пользователь удалён")
@bot.message_handler(commands=['registration'])
def start(message):
    bot.send_message(message.from_user.id,"Имя")
    bot.register_next_step_handler(message,get_name) #следующий шаг – функция get_name
def get_name(message): #получаем фамилию
    global name
    name=message.text
    bot.send_message(message.from_user.id,"Фамилия")
    bot.register_next_step_handler(message,get_surname)
def get_surname(message):
    global surname
    surname=message.text
    bot.send_message(message.from_user.id,"Возраст")
    bot.register_next_step_handler(message,get_age)
def get_age(message):
    global age
    try:
        age=int(message.text) #проверяем, что возраст введен корректно
        if age<=0:
            bot.send_message(message.from_user.id,"Некорректный возраст, попробуйте ещё раз")
            bot.register_next_step_handler(message,get_age)
    except Exception:
        bot.send_message(message.from_user.id,"Некорректный возраст, попробуйте ещё раз")
        bot.register_next_step_handler(message,get_age)
    

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, "Я могу:\n/registration - регистрация пользователя\n/information - информация о разработчике\n/delete_user - удаление пользователя\n\nкто я? - показать данные пользователя\nкарта - дать ссылку на сервис Яндекс-карты\nпогода - дать ссылку на сервис Яндекс-погода\ne-mail - дать ссылки на сервисы Яндекс-почта и Гугл-почта\n\nСпасибо, что пользуетесь моими услугами!")
@bot.message_handler(commands=['information'])
def start_message(message):
    bot.send_message(message.chat.id,"Бот разработан студентом Чижом Степаном Анатольевичем из группы БОС1901. Предмет: Информатика")

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower()=="кто я?":
        if age==0:
            bot.send_message(message.from_user.id,"Пожалуйста, пройдите регистрацию!")
        else:
            bot.send_message(message.from_user.id,"Вам "+str(age)+" лет, Вас зовут "+name+" "+surname)
    elif message.text.lower()=="карта":
        bot.send_message(message.chat.id,"Если Вам нужна карта, перейдите по следующей ссылке:\nhttps://yandex.ru/maps")
    elif message.text.lower()=="погода":
        bot.send_message(message.chat.id,"Если Вам нужен прогноз погоды, перейдите по следующей ссылке:\nhttps://yandex.ru/pogoda")
    elif message.text.lower()=="e-mail":
        bot.send_message(message.chat.id,"Если Вам нужна электронная пачта, перейдите по следующим ссылкам:\nhttps://mail.yandex.ru\n https://mail.google.com")
    # elif message.text.lower()=="игра":
    #     bot.send_message(message.chat.id,"В какую игру Вы хотите со мной сыграть?\
    #     \nВведите \"КНБ\", чтобы начать играт в камень-ножницы-бумага")
    #     bot.register_next_step_handler(message,game1)   
    else:
        bot.send_message(message.from_user.id,"Я Вас не понимаю")

# a1=""
# @bot.message_handler(content_types=['text'])
# def for_play(message):
#     from random import randint
#     global a1
#     global gamer
#     global tbot
#     a1=message.text
#     options={1:"камень",2:"ножницы",3:"бумага"}
#     a2=str(options.get(randint(1,4)))
#     bot.send_message(message.chat.id,"Мой выбор: "+a2)
#     if a1==a2:
#         bot.send_message(message.chat.id,"Ничья. Ещё раз")
#     elif (a1=="камень" and a2=="ножницы") or \
#     (a1=="ножницы" and a2=="бумага") or \
#     (a1=="бумага" and a2=="камень"):
#         gamer+=1
#         bot.send_message(message.chat.id,"Неплохо, Вам очко")
#     elif (a1=="камень" and a2=="бумага") or \
#     (a1=="ножницы" and a2=="камень") or \
#     (a1=="бумага" and a2=="ножницы"):
#         tbot+=1
#         bot.send_message(message.chat.id,"Ура! Очко мне)")
#     else:
#         bot.send_message(message.chat.id,"Извините, я не понял что вы написали. Ещё раз!")
#     bot.register_next_step_handler(message,game1)

# gamer=tbot=0
# def game1(message):
#     bot.send_message(message.chat.id,"Правила: пишите одно слово из трёх, "\
#     "а я буду случайным отвечать Вам. "\
#     "Камень бьёт ножницы, ножницы - бумагу, "\
#     "бумага - камень. Играем до трёх побед.")
#     global gamer
#     global tbot
#     global a1
#     while gamer<3 or tbot<3:
#         bot.send_message(message.from_user.id,"Ваш ход:")
#         bot.register_next_step_handler(message,for_play)   
#     if gamer>tbot:
#         bot.send_message(message.chat.id,"Эх, Вы победили со счётом "+str(gamer)+\
#         ":"+str(tbot)+".\nНо ничего, в следующий раз я обязательно выиграю!")
#     else:
#         bot.send_message(message.chat.id,"Ура, я выиграл со счётом "+str(tbot)+\
#         ":"+str(gamer)+"!\nНо не расстраивайтесь, в следующий раз и Вам повезёт")
#     gamer=tbot=0


bot.polling(none_stop=True,interval=2)