# encoding: utf-8
import telebot
from telebot import types
from datetime import datetime
import sys

token = raw_input('Digite o token do seu chatbot:')
bot = telebot.TeleBot(token)

now = datetime.now()
hora = now.hour 
if(hora>6 and hora<12):
	msg = "Bom dia."
elif(hora>12 and hora<18):
	msg = "Boa Tarde."
else:
	msg = "Desculpe não podemos lhe responder agora, nosso horário de atendimento é de 08:00 á 12:00 e de 13:00 á 18:00."

# sys.exit(), testes
# msg="Boa noite", testes

# Atendimento Inicial
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	
	if(msg!="Desculpe não podemos lhe responder agora, nosso horário de atendimento é de 08:00 á 12:00 e de 13:00 á 18:00."):
		bot.reply_to(
			message, msg+", Seja bem vindo ao atendimento da Bleez.\n\n"
			"Você está no autoatendimento da Bleez. Este"
			" menu inicial é automático.\n"
			"\n Digite ou clique nos comandos para prosseguir:\n"
			"/Planos - Para aderir aos planos\n"
			"/Suporte - Suporte Técnico\n"
			"/Finalizar - Finalizar atendimento"
		)
	else:
		bot.reply_to(message, msg)
		bot.reply_to(
			message, "Agradecemos seu contato\n\n"
			"Siga a Bleez e acompanhe nossas ações...\n\n"
			"Instagram\n"
			"https://www.instagram.com/bleezecommerce/\n\n"
			"Nossos contatos:\n"
			"85 0000-0000"
		)

# Primeiro menu de opções do cliente
@bot.message_handler(commands=['Planos'])
def echo_all(message):
	bot.reply_to(
		message, "Escolha o melhor Plano pro seu negócio\n\n"
		"O Bleez Shop tem planos preparados pra atender o seu negócio de acordo com o seu nível de maturidade no e-commerce. Se você precisa validar seu negócio (Basic), se você precisa alavancar suas vendas (Pro), ou até mesmo se você precisa de uma operação exclusiva e robusta (Exclusive).\n\n"
		"Para mais informações acesse:\n"
		"https://bleez.com.br/plataforma-de-ecommerce-em-fortaleza/"

	)

@bot.message_handler(commands=['Finalizar'])
def echo_all(message):
	bot.reply_to(message, "Agradecemos seu contato\n\n"
			"Siga a Bleez e acompanhe nossas ações...\n\n"
			"Instagram\n"
			"https://www.instagram.com/bleezecommerce/\n\n"
			"Nossos contatos:\n"
			"85 0000-0000")


@bot.message_handler(commands=['Suporte'])
def echo_all(message):
	bot.reply_to(message, "Suporte print")

	
bot.polling()