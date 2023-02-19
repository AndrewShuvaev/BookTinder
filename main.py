import telebot
import random
from telebot import types
from telebot.types import ReplyKeyboardMarkup


bot = telebot.TeleBot("6193228135:AAG_ORvvAJ0wLh_S5iE-9wQKmWKLmN3GIzk")
@bot.message_handler(commands=['start'])
def send_welcome(message):

	warkup = types.InlineKeyboardMarkup()
	warkup.add(types.InlineKeyboardButton("вот он 👈", url="https://igraslov.store/"))

	photo = open('logo.webp', 'rb')
	bot.send_photo(message.chat.id, photo, caption=f'Здравствуйте, \nВы пользуетесь ботом магазина Игра Слов, бот будет рекомендовать Вам книги, для это нажмите на кнопку ниже, так же вы сможете приобрести понравившиеся книги')

	bot.send_message(message.chat.id, 'Так же обязательно посетите наш сайт!', reply_markup=warkup)
	bot.send_message(message.chat.id, 'Список команд /help')

@bot.message_handler(commands=['help'])
def send_help(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	but1 = types.KeyboardButton('Рекомендации')
	but2 = types.KeyboardButton('Статистика')
	markup.add(but1, but2)
	bot.send_message(message.chat.id, 'Полный список команд:'
									  '\n 1. Рекомендации- ознакомиться с предложеннными книгами'
									  '\n 2. Статистика- вы сможете просмотреть книги, которые вы оценили',reply_markup=markup)

@bot.message_handler(chat_types=["private"], func=lambda msg: msg.text == "Рекомендации")
def if_sp(message: types.Message):

	markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	markup.row('Читал, классная', 'Читал, не очень', 'Не читал, но хочу', 'Не читал, не хочу', 'Подробнее о книге')

	sarkup = types.InlineKeyboardMarkup()
	sarkup.add(types.InlineKeyboardButton("796,00₽",url="https://igraslov.store/product/kitaj-i-okrestnosti-mifologiya-folklor-literatura-rggu-tverd/"))

	china = open('492fbb33-82d6-45b3-a1aa-0e1351962523_9cf6529d-66e9-4c67-849b-a1b2a641c60b.webp', 'rb')
	bot.send_photo(message.chat.id, china, caption=f'Китай и окрестности. Мифология, фольклор, литература')
	bot.send_message(message.chat.id, 'Купить', reply_markup=sarkup)
	bot.send_message(message.chat.id, 'Оцените книгу', reply_markup=markup)

@bot.message_handler(chat_types=["private"], func=lambda msg: any([
    msg.text == 'Читал, классная',
    msg.text == 'Читал, не очень',
    msg.text == 'Не читал, но хочу',
    msg.text == 'Не читал, не хочу',
    msg.text == 'Подробнее о книге']))
def if_sp(message: types.Message):

	markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	markup.row('Читал, классная', 'Читал, не очень', 'Не читал, но хочу', 'Не читал, не хочу', 'Подробнее о книге')

	sarkup = types.InlineKeyboardMarkup()
	sarkup.add(types.InlineKeyboardButton("834,00 ₽", url="https://igraslov.store/product/kitaj-i-okrestnosti-mifologiya-folklor-literatura-rggu-tverd/"))

	china = open('1a08c3f6-ab89-4c99-848b-fec0f5d2c3cf_6364a347-1f0e-44a7-8e13-10796af87892.webp', 'rb')
	bot.send_photo(message.chat.id, china, caption=f'Горо Х. Японская цивилизация')
	bot.send_message(message.chat.id, 'Купить', reply_markup=sarkup)
	bot.send_message(message.chat.id, 'Оцените книгу', reply_markup=markup)


bot.polling(none_stop=True)