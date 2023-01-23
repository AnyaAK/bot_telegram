from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext import InlineQueryHandler

from telegram.chataction import ChatAction

from uuid import uuid4

from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import InputTextMessageContent
from telegram import InlineQueryResultArticle
updater = Updater('5967740584:AAHVjCtwz_5FjYqmjn4arPytiOgqmAJ70Zs')

def start(bot, update):
    #import pdb; pdb.set_trace()
    chat_id=update.message.chat_id
    first_name=update.message.chat.first_name
    last_name=update.message.chat.last_name

    bot.send_chat_action(chat_id, ChatAction.TYPING)
    bot.sendMessage(chat_id, 'Hello {}  {} Welcome!'.format(first_name , last_name))

def service_keyboard(bot,update):
    chat_id=update.message.chat_id
    keyboard=[
                 ['chemical engineering']
                 ['civil engineering'],['mechanical engineering']
                 ['Computer Engineering'],['electrical engineering'],['Materials Engineering']
             ]
    bot.sendMessage(chat_id , 'Select your interest', reply_markup= ReplyKeyboardMarkup
    (keyboard , resize_keyboard=True , one_time_keyboard=True))

def favor_keyboard(bot, update):
    chat_id=update.message.chat_id
    keyboard=[
               [
                
                InlineKeyboardButton('chemical engineering', callback_data = '1'),
                InlineKeyboardButton('mechanical engineering', callback_data = '2')

               ]
             ]
    bot.sendMessage(chat_id,'Similar', reply_markup=InlineKeyboardMarkup(keyboard))

def favor_handler_botton(bot , update):
    query = update.callback_query
    data = query.data
    chat_id = query.message.chat_id
    message = query.message.message_id
    description = 'the information you want is {}'.format(data)

    if data='1':
        description = 'I can tell you about Chemical engineering job market around the world.'
    elif data='2':
        description = 'I can tell you about Mechanical engineering job market around the world.'

    bot.editMessageText(text = description , chat_id = chat_id , message_id = message_id)


def feature_inline_query(bot, update):
    query = update.inline_query.query
    results = list()
    results.append(InlineQueryResultArticle(id = uuid4() , title = 'Uppercase' ,
    input_message_content = InputTextMessageContent(query.upper()) ))
    results.append(InlineQueryResultArticle(id = uuid4() , title = 'Lowercase' ,
    input_message_content = InputTextMessageContent(query.lower()) ))

    bot.answerInlineQuery(results = results)


def send_photo(bot, update):
    chat_id = update.message.chat_id
    bot.send_chat_action(chat_id , ChatAction.UPLOAD_PHOTO)
    photo = open('./img/robot.jpg' , 'rb')
    bot.sendPhoto(chat_id , photo , 'This is the photo :D ')
    photo.close()


def send_document(bot , update):
    chat_id = update.message_id.chat_id
    bot.send_chat_action(chat_id , ChatAction.UPLOAD_DOCUMENT)
    doc = open('./other/sourse.txt', 'rb')
    bot.sendDocument(chat_id, doc , 'This is my sourse :D ')
    doc.close()


start_command = CommandHandler('start', start)
service_command = CommandHandler('service', service_keyboards)
favor_command = CommandHandler('favor', favor_keyboard)
favor_handler = CallbackQueryHandler(favor_handler_botton)
feature_handler = InlineQueryHandler(feature_inline_query)
photo_command = CommandHandler('photo' , send_photo)
document_command = CommandHandler('doc' , send_document)

updater.dispatcher.add_handler(start_command)
updater.dispatcher.add_handler(service_command)
updater.dispatcher.add_handler(favor_command)
updater.dispatcher.add_handler(favor_handler)
updater.dispatcher.add_handler(feature_handler)
updater.dispatcher.add_handler(photo_command)
updater.dispatcher.add_handler(document_command)

updater.start_polling()
updater.idle()
