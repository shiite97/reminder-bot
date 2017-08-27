# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler
import config


def start(bot, update):
    update.message.reply_text('Hey, {}! {}'.format(update.message.from_user.first_name, ', glad to see you!'))


def stop(bot, update):
    update.message.reply_text('Hope to see you back again, {}!'.format(update.message.from_user.first_name))


def echo(bot, update):
    update.message.reply_text(update.message.text)


updater = Updater(config.token)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('stop', stop))
updater.dispatcher.add_handler(MessageHandler('', echo))

updater.start_polling()
updater.idle()
