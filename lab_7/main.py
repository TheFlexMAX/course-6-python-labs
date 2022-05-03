from datetime import datetime, timedelta

import telebot
import psycopg2

from telebot import types

from consts import rus_day_of_week_short, rus_day_of_week
from helpers import row_prettier, week_schedule_prettier, day_of_week_to_short
from queries import in_this_week_query, on_day_of_week

token = "BOT_TOKEN"
bot = telebot.TeleBot(token)
conn = psycopg2.connect(
    database="lab_7",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5433"
)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу")
    keyboard.row("GitLab", "GitHub")
    keyboard.row("Дай банан")
    keyboard.row("/help")
    keyboard.row("/schedule")
    bot.send_message(
        message.chat.id, 'Привет! Хочешь узнать свежую информацию о колледже Сервер при МАУП?', reply_markup=keyboard
    )


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею...')
    bot.send_message(message.chat.id, '1. Давать ссылку на GitLab')
    bot.send_message(message.chat.id, '2. Давать ссылку на GitHub')
    bot.send_message(message.chat.id, '3. Показывать банан')
    bot.send_message(message.chat.id, '4. Показывать расписание')


@bot.message_handler(commands=['schedule'])
def scheduler(msg):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Понедельник")
    keyboard.row("Вторник")
    keyboard.row("Среда")
    keyboard.row("Четверг")
    keyboard.row("Пятница")
    keyboard.row("Неделя", "След неделя")
    bot.send_message(
        msg.chat.id, 'Выберите, за какой период времени вы хотите видеть расписание', reply_markup=keyboard
    )


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
    elif text == "неделя":
        week_schedule(message, 'this')
    elif text == "след неделя":
        week_schedule(message, 'next')
    elif text in [day_of_week.lower() for day_of_week in rus_day_of_week]:
        day_schedule(message, text)
    else:
        bot.send_message(message.chat.id, 'Извините, я Вас не понял')


def week_schedule(msg, period: str):
    today = datetime.now()

    if period == 'this':
        start = (today - timedelta(days=today.weekday()))
        end = start + timedelta(days=6)
    else:
        start = (today - timedelta(days=today.weekday()) + timedelta(days=7))
        end = start + timedelta(days=7)

    cursor = conn.cursor()
    cursor.execute(in_this_week_query, (str(start.date()), str(end.date())))
    data = cursor.fetchall()

    res_schedule_week = {
        'Пн': [],
        'Вт': [],
        'Ср': [],
        'Чт': [],
        'Пт': [],
        'Сб': [],
        'Вс': [],
    }
    for row in data:
        day = rus_day_of_week_short[row[0].weekday()]
        res_schedule_week[day].append(row_prettier(row))

    bot.send_message(msg.chat.id, week_schedule_prettier(res_schedule_week))


def day_schedule(msg, day_of_week: str):
    today = datetime.now()
    day_of_week_short = day_of_week_to_short(day_of_week)
    day_index = rus_day_of_week_short.index(day_of_week_short)

    start = (today - timedelta(days=today.weekday()))
    day = start + timedelta(days=day_index)

    cursor = conn.cursor()
    cursor.execute(on_day_of_week, (str(day.date()),))
    data = cursor.fetchall()

    res_schedule_week = {
        day_of_week_short: []
    }

    for row in data:
        res_schedule_week[day_of_week_short].append(row_prettier(row))

    bot.send_message(msg.chat.id, week_schedule_prettier(res_schedule_week))


def main():
    bot.polling()


if __name__ == '__main__':
    main()
