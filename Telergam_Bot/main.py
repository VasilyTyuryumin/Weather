import telebot
import requests
import json

bot = telebot.TeleBot('6282635487:AAFSoinH0BypefumCjInMyE0XdKIbt0G-A4')
API = '7ca77fbb7a41b630c28d486122ec6797'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города для погоды')


@bot.message_handler(content_types=['text'])
def getweather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')

       # image = 'sun.jpg' if temp > 5.0 else 'sun_cloudy.jpg'
      # file = open('./' + image, 'rb')
       # bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Город указан неверно')

bot.polling(none_stop=True)
