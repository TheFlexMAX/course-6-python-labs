import telebot

from telebot import types

token = "BOT_TOKEN"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу")
    keyboard.row("GitLab", "GitHub")
    keyboard.row("Дай банан")
    keyboard.row("/help")
    bot.send_message(
        message.chat.id, 'Привет! Хочешь узнать свежую информацию о колледже Сервер при МАУП?', reply_markup=keyboard
    )


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею...')
    bot.send_message(message.chat.id, '1. Давать ссылку на GitLab')
    bot.send_message(message.chat.id, '2. Давать ссылку на GitHub')
    bot.send_message(message.chat.id, '3. Показывать банан')


@bot.message_handler(content_types=['text'])
def answer(message):
    text = message.text.lower()
    if text == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда - https://server.odessa.ua/')
    elif text == "gitlab":
        bot.send_message(message.chat.id, 'https://gitlab.com/TheFlexMAX')
    elif text == "github":
        bot.send_message(message.chat.id, 'https://github.com/TheFlexMAX')
    elif text == "дай банан":
        bot.send_message(message.chat.id, 'На')
        bot.send_message(message.chat.id, '🍌')
    else:
        bot.send_message(message.chat.id, 'Неизвестная команда')



def main():
    bot.polling()


if __name__ == '__main__':
    main()
