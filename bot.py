from email import message
from telegrambot.config import *
import telebot
import requests
import threading

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start","test"])
def cmd_start(message):
    bot.send_message(-1001523347078, "hola:D") #-1001880307694



def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def foo():
    response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")

    a = response.json()

    priceBTC = a["price"]
    price = int(float(priceBTC))
    a = str(price)
  
    bot.send_message(-1001523347078, "OMAR SE LA COME")#"BTC: "+ a)

# using
setInterval(foo,0.5)

if __name__ == "__main__":
  print("iniciando")
  bot.infinity_polling()
  print("Fin")