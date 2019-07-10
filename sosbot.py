#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler
import random

updater = Updater(token='856780096:AAF1AM5dxXxNXWxZLzk8Do87iFoIGD88kco')
dispatcher = updater.dispatcher


def hola(bot, update):
    llista_salutacions = ['Hola','Bones','Què tal?']
    r = len(llista_salutacions)
    m = random.randint(0,r)
    missatge = llista_salutacions[m]
    bot.send_message(chat_id=update.message.chat_id, text=missatge)


def adeu(bot, update):
    llista_comiats = ['Adéu', 'Fins aviat!','A reveure!']
    r = len(llista_comiats)
    m = random.randint(0,r)
    missatge = llista_comiats[m]
    bot.send_message(chat_id=update.message.chat_id, text=missatge)


saluda_handler = CommandHandler('hola',hola)
acomiada_handler = CommandHandler('adeu', adeu)

handlers = [CommandHandler('hola',hola), CommandHandler('adeu',adeu)]

for handler in handlers:
    dispatcher.add_handler(handler)

updater.start_polling()
