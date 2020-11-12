id = 802883577

TOKEN = '1433400975:AAHsqEuPyDAyUxCK1v7n4TjI7J-89vJ72zU'

import telebot

bot = telebot.TeleBot(TOKEN)

bot.send_message(id,'Ending Workflow')
resu = open("res.txt","rb").read()
result = open("res.txt","r").read()
bot.send_message(id,'Results of scan Saved: ')
mass = result.split('\n')
start = 0
end = len(mass)
bot.send_message(id,'Results can be viewed at https://raw.githubusercontent.com/Kamakepar2029/allnerwork/main/res.txt')
bot.send_message(id,mass[0])
bot.send_message(id,mass[1])
bot.send_message(id,mass[2])
bot.send_message(id,mass[3])
bot.send_message(id,mass[4])
bot.send_message(id,mass[5])
file = open('res.txt', 'rb')
bot.send_document(id, file)
id = 828539867
bot.send_message(id,'Ending Workflow')
resu = open("res.txt","rb").read()
result = open("res.txt","r").read()
bot.send_message(id,'Results of scan Saved: ')
mass = result.split('\n')
start = 0
end = len(mass)
bot.send_message(id,'Results can be viewed at https://raw.githubusercontent.com/Kamakepar2029/allnerwork/main/res.txt')
bot.send_message(id,mass[0])
bot.send_message(id,mass[1])
bot.send_message(id,mass[2])
bot.send_message(id,mass[3])
bot.send_message(id,mass[4])
bot.send_message(id,mass[5])
file = open('res.txt', 'rb')
bot.send_document(id, file)


bot.send_document(id, result)
bot.send_document(id, "FILEID")
bot.send_message(id,resu)
