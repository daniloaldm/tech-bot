# encoding: utf-8
import telebot
from telebot import types

token = raw_input('Digite o token do seu chatbot:')
bot = telebot.TeleBot(token) 

# Mensagem Inicial
@bot.message_handler(commands=['start', '9'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup()
	itembtn1 = types.KeyboardButton('/1')
	itembtn2 = types.KeyboardButton('/2')
	itembtn3 = types.KeyboardButton('/3')
	itembtn4 = types.KeyboardButton('/4')
	itembtn5 = types.KeyboardButton('/5')
	itembtn6 = types.KeyboardButton('/6')
	itembtn7 = types.KeyboardButton('/7')
	itembtn8 = types.KeyboardButton('/8')
	itembtn9 = types.KeyboardButton('/9')

	markup.row(itembtn1, itembtn2, itembtn3)
	markup.row(itembtn4, itembtn5, itembtn6)
	markup.row(itembtn7, itembtn8, itembtn9)
	bot.reply_to(message, "Olá, como posso ajudar?"
	"\n1 - Como abrir e acompanhar tickets?"
	"\n9 - Exibir Opções",
	reply_markup=markup)

# Opções do cliente
@bot.message_handler(commands=['1'])
def echo_all_cupom(message):
	bot.reply_to(message, "https://bleez.zendesk.com/hc/pt-br/articles/360033185432-Como-abrir-e-acompanhar-tickets-")

bot.polling()