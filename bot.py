import telebot
import config
from telebot import types
bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start'])
def welcome(message):
    

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Розклад на тиждень")
    item2 = types.KeyboardButton("Розклад на місяць")

    markup.add(item1, item2)



    bot.send_message(message.chat.id,"Вітаю, {0.first_name}!👋\nЯ - <b>{1.first_name}</b>, Радий вас бачити😀\nЯ бот який допоможе дізнатися розклад занять".format(message.from_user, bot.get_me()), 
        parse_mode='html', reply_markup=markup)   



@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Розклад на тиждень':
            sti = open('C:/Users/1/Desktop/Telegram/tizden.PNG', 'rb')
            bot.send_photo(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Розклад на тиждень📅')
        elif message.text == 'Розклад на місяць':
            sti = open('C:/Users/1/Desktop/Telegram/misas.PNG', 'rb')
            bot.send_photo(message.chat.id, sti)
            bot.send_message(message.chat.id, 'Розклад на місяць🗓')
        else:
            bot.send_message(message.chat.id, 'Не знаю що відповісти')
bot.polling(none_stop=True)