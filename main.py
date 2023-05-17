import poe
import logging
import sys
import telebot

#send a message and stream the response

poe_token = "zW36rqQHeYCJVqleOMQIcA%3D%3D"
telegram_token = "5807020635:AAFQPDeYlf8AF81UxpBJ2hkbm4daXiCpb8g"
poe.logger.setLevel(logging.INFO)
client = poe.Client(poe_token)
bot = telebot.TeleBot(telegram_token)

message = "Hello"

def getandsend_massage(message):
  response = ""
  for chunk in client.send_message("capybara", message, with_chat_break=True):
     response += chunk["text_new"]
  return response

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, getandsend_massage(message.text))


bot.infinity_polling()
