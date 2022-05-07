import lxml
from bs4 import BeautifulSoup
import requests
import telebot
from Token import TOKEN
from telebot import types


def weather_now():
    url = "https://world-weather.ru/pogoda/kazakhstan/almaty/10days/"
    r = requests.get(url=url)
    soup = BeautifulSoup(r.text, "lxml")
    weather_temperature = soup.find("tr", class_="day").find("td", class_= "weather-feeling").text
    return weather_temperature


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])

def welcome(message):
    sti = open('welcome/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    button1 = types.KeyboardButton('♂ Yes, sir! ♂')
    button2 = types.KeyboardButton('No, thanks!')

    markup.add(button1, button2)
    bot.send_message(message.chat.id,
                     "♂Welcome to the club, buddy!♂  Do you want to see the weather in Almaty?".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
    # ---------------------------------------------------------------------------

def answer(message):
    if message.chat.type == 'private':
        if message.text == '♂ Yes, sir! ♂':
            text = 'Weather outside: ' + weather_now()

                # keyboard (Создание кнопок под текстом)
            markup = types.InlineKeyboardMarkup(row_width=2)
            bot.send_message(message.chat.id, text , parse_mode='Markdown', reply_markup=markup)

            # elif message.text == ' '
        elif message.text == "No, thanks!":
            bot.send_message(message.chat.id, "Have a good day")


        else:
            bot.send_message(message.chat.id, 'Wee-wee')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:

                # keyboard (Работа с кнопками под текстом)
            if call.data == '1':
                bot.send_message(call.message.chat.id, 'Wee-wee')
            elif call.data == '2':
                bot.send_message(call.message.chat.id, 'Wee-wee')
            elif call.data == '3':
                bot.send_message(call.message.chat.id, 'Wee-wee')
            elif call.data == '4':
                bot.send_message(call.message.chat.id, 'Wee-wee')

                # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="Wee-wee",
                                reply_markup=None)

                # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                text="Yeah")

    except Exception as e:
        print(repr(e))


bot.polling()

