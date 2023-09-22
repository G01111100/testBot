import telebot
from telebot import types

tokenStr = '6407233345:AAGbHFYDhak-7r6c8RmuLuEovFA8Ha5vbho'
bot = telebot.TeleBot(tokenStr)
language = 0

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🇷🇺 Русский')
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Здравствуйте! / Hello!")
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык: / 🇬🇧 Choose your language:", reply_markup=markup)

@bot.message_handler(commands=['menu'])
def menu(message):
    global language
    if language == 1:
        bot.send_message(message.from_user.id, 'Один')

    elif language == 2:
        bot.send_message(message.from_user.id, 'One')

    else:
        bot.send_message(message.from_user.id, 'Error')

@bot.message_handler(commands=['language'])
def language(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🇷🇺 Русский')
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, '🇷🇺 Выберите язык / 🇬🇧 Choose your language', reply_markup=markup)

@bot.message_handler(commands=['botfatherlink'])
def btnlink(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Bot Father', url='https://t.me/BotFather')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "You can find my Father here!", reply_markup=markup)

@bot.message_handler(commands=['botlink'])
def link(message):
    bot.send_message(message.from_user.id, 'My address: https://t.me/oneTwoFourTestBot')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # bot.send_message(message.from_user.id, "GOOD!")
    global language
    if message.text == '🇷🇺 Русский':
        language = 1
        bot.send_message(message.from_user.id, 'Язык: Русский')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Один')
        btn2 = types.KeyboardButton('Два')
        btn3 = types.KeyboardButton('Три')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Выберите:", reply_markup=markup)

    elif message.text == '🇬🇧 English':
        language = 2
        bot.send_message(message.from_user.id, 'Language: English')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('One')
        btn2 = types.KeyboardButton('Two')
        btn3 = types.KeyboardButton('Three')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Choose:", reply_markup=markup)

    elif message.text == 'Один' or message.text == 'One':
        bot.send_message(message.from_user.id, '1')

    elif message.text == 'Два' or message.text == 'Two':
        bot.send_message(message.from_user.id, '2')

    elif message.text == 'Три' or message.text == 'Three':
        bot.send_message(message.from_user.id, '3')


bot.polling(none_stop=True, interval=0)
