# encoding: utf-8
import telebot
from datetime import datetime
import sys
import logging

# Gerando logs diários
datefile = datetime.today().date()
filename = "log/"+"{}.txt".format(datefile)
logging.basicConfig(filename=filename, level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

token = raw_input('Digite o token do seu chatbot:')
# token = '' # faço pra testar
bot = telebot.TeleBot(token)

now = datetime.now()
hora = now.hour
if(hora>6 and hora<12):
	msg = "Bom dia."
elif(hora>12 and hora<18):
	msg = "Boa Tarde."
else:
	msg = "Desculpe não podemos lhe responder agora, nosso horário de atendimento é de 08:00 á 12:00 e de 13:00 á 18:00."

# Atendimento Inicial
@bot.message_handler(commands=['start', 'ajuda'])
def send_welcome(message):

	if(msg!="Desculpe não podemos lhe responder agora, nosso horário de atendimento é de 08:00 á 12:00 e de 13:00 á 18:00."):
		bot.reply_to(
			message, msg+" Seja bem vindo ao atendimento da Bleez.\n\n"
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
			"85 3025-3315"
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
			"85 3025-3315")


@bot.message_handler(commands=['Suporte'])
def echo_all(message):
	bot.reply_to(
				message, "\n Digite ou clique nos comandos para prosseguir:\n"
				"/Contato - Para entrar em contato com um de nossos atendentes.\n"
				"/Ticket - Como abrir e acompanhar tickets?\n"
				"/Whatsapp - Como adicionar o ícone de WhatsApp na minha loja?\n"
				"/Cupom - Como criar cupons de desconto?\n\n"
				
				"Caso sua dúvida não seja relacionado a uma das mais frequentes citadas acima, segue o link para as perguntas frequentes:\n"
				"https://bleez.zendesk.com/hc/pt-br/categories/360000688751-Perguntas-Frequentes\n\n"

				"Caso sua dúvida ou problema não esteja listada por favor digite ou clique no comando /Contato para entrar em contato."

				
			)

@bot.message_handler(commands=['Contato'])
def echo_all(message):
	bot.reply_to(
				message, "Telefone para contato direto:\n"
				"85 3025-3315"
			)

@bot.message_handler(commands=['Ticket'])
def echo_all(message):
	bot.reply_to(
				message, "https://bleez.zendesk.com/hc/pt-br/articles/360033185432-Como-abrir-e-acompanhar-tickets-"
			)

@bot.message_handler(commands=['Whatsapp'])
def echo_all(message):
	bot.reply_to(
				message, "https://bleez.zendesk.com/hc/pt-br/articles/360035448071-Como-adicionar-o-%C3%ADcone-de-WhatsApp-na-minha-loja-\n"
			)

@bot.message_handler(commands=['Cupom'])
def echo_all(message):
	bot.reply_to(
				message, "https://bleez.zendesk.com/hc/pt-br/articles/360033379972-Como-criar-cupons-de-desconto-\n"
			)


@bot.message_handler()
def echo_all(message):
	# Mensagem do usuário que não é comando
	print message.json['text'],"\n\n"

	#Id do usuário
	print message.json['from']['id'],"\n\n"

	#Dados que seria uma boa guardar
	print message.json,"\n\n"

	bot.reply_to(
		message, "Desculpe, não consigo compreender o comando, para exibir as opções digite ou clique /ajuda"
	)

bot.polling()

# Próximos passos
# Como criar comando de startChamado e finalizarChamado
# Como python esperar o finalizar chamado para pegar msg concatenar toda e abrir como ticket
# Como pegar upload de img
# Abrir ticket pelo próprio telegram, enviando email para suporte@bleez
# Gerar log das conversas
