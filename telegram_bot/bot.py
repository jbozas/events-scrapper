import datetime

import telebot
from events.models import Event
from EventsScrapper import settings

bot = telebot.TeleBot(settings.T_BOT_TOKEN, parse_mode='HTML')

commands = {
    'start': 'A simple description about myself.',
    'help': 'Get the available commands.',
    'movies': 'Get a list of all movies.',
    'today': 'Get a list of today movies.',
    'tomorrow': 'Get a list of tomorrow movies.',
}


class TelegramBot(object):

    def __init__(self):
        self.bot = bot

    @bot.message_handler(commands=['start'])
    def on_welcome(message):
        bot.reply_to(
            message, f"Hi! My name is <b>ShowMan</b>. \nI'm an events bot. \nType /help to show you what can I do...")

    @bot.message_handler(commands=['help'])
    def on_help(message):
        help_text = "The following commands are available: \n"
        for key in commands:  # generate help text out of the commands dictionary defined at the top
            help_text += "/" + key + ": "
            help_text += commands[key] + "\n"
        bot.reply_to(message, help_text)

    @bot.message_handler(commands=['movies'])
    def on_movies(message):
        event = Event.objects.last().get_data
        bot.reply_to(message, f"{event}")

    @bot.message_handler(commands=['today'])
    def on_today(message):
        """
        Returns a specific the movies programmed for today.
        """
        today = datetime.datetime.now()
        events = Event.objects.filter(
            datetime__month=today.month,
            datetime__day=today.day,
            datetime__year=today.year,
        )
        bot.reply_to(
            message, f"There are <b>{events.count()}</b> movies to watch today...")
        for event in events:
            if not event.old:
                msg = f"<b>{event.movie.title}</b> on {event.cinema.html_name} at {event.scheduled}"
                bot.reply_to(message, msg)

    @bot.message_handler(commands=['tomorrow'])
    def on_tomorrow(message):
        """
        Returns a specific the movies programmed for tomorrow.
        """
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
        events = Event.objects.filter(
            datetime__month=tomorrow.month,
            datetime__day=tomorrow.day,
            datetime__year=tomorrow.year,
        )
        bot.reply_to(
            message, f"There are <strong>{events.count()}</strong> movies to watch tomorrow...")
        for event in events:
            msg = f"<b>{event.movie.title}</b> on {event.cinema.name} at {event.scheduled}"
            bot.reply_to(message, msg)

    def run(self):
        print('Bot running...')
        self.bot.polling()
