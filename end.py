id = 802883577

TOKEN = '1433400975:AAHsqEuPyDAyUxCK1v7n4TjI7J-89vJ72zU'

import telebot

bot = telebot.TeleBot(TOKEN)

bot.send_message(id,'Ending Workflow')
resu = open("res.txt","r").read()
bot.send_message(id,'Results of scan Saved: ')
mass = resu.split('\n')
start = 0
end = len(mass)
while start<end:
  bot.send_message(id,mass[start])
  start+=1

bot.send_message(id,resu)
