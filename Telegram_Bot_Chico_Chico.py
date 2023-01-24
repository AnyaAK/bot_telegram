import telebot
import time
from telebot.types import InlineKeyboardButton , InlineKeyboardMarkup
token = "5967740584:AAHVjCtwz_5FjYqmjn4arPytiOgqmAJ70Zs"
bot = telebot.TeleBot(token = "5967740584:AAHVjCtwz_5FjYqmjn4arPytiOgqmAJ70Zs")

def markup_inline():
  markup=InlineKeyboardMarkup()
  markup.width = 2
  markup.add(
      InlineKeyboardButton("About Us" , callback_data = "1"),
      InlineKeyboardButton("Pin code" , callback_data = "2")
  )
  return markup
@bot.message_handler(commands=['start', 'hello'])
def start_user(message):
  name=message.chat.first_name
  bot.send_message(message.chat.id, "Hello " + name +" !" " I'm Chico Chico🙋" , reply_markup = markup_inline())
  bot.send_message(message.chat.id, "Select /greet , /register or /instagram")

@bot.callback_query_handler(func = lambda message:True)
def callback_query(call):
  if call.data == "1":
    bot.answer_callback_query(call.id , "Created by Farid & Anya")
  if call.data =="2":
    bot.answer_callback_query(call.id , "any six digit number")

@bot.message_handler(commands=['register'])
def register(message):
  msg=bot.send_message(message.chat.id, "inter your pin code: ")
  bot.register_next_step_handler(msg , pin_code_step)

def pin_code_step(message):
  pin=message.text
  if pin in ['000000' , '111111'] or not len(pin)==6:
    bot.send_message(message.chat.id,"Pin is incorrect☹️")
  else:
    bot.send_message(message.chat.id,"Registered👌")


@bot.message_handler(commands=['greet'])
def greet_user(message):
  bot.reply_to(message, "How are you dude?😃")

def find_at(msg):
    for text in msg:
        if '@' in text:
            return text

@bot.message_handler(commands=['instagram'])
def send_help(message):
    bot.reply_to(message , 'Send me a username (started with @)')

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def answer(message):
    text = message.text.split()
    at_text = find_at(text)

    bot.reply_to(message ,'https://instagram.com/{}'.format(at_text[1:]))

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
