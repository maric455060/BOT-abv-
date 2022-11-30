from telegram import Bot
 from telegram.ext import Updater, MessageHandler, Filters

 bot = Bot(token='5726183817:AAFl_Bkd6u-5g2qNwQSlzf5UpwfET54satc')
 updater = Updater(token='5726183817:AAFl_Bkd6u-5g2qNwQSlzf5UpwfET54satc')
 dispahather = updater.dispatcher

 def start(update, context):
     text = update.message.text.split()
     list = []
     for ward in text:
          if 'абв' not in ward:
             list.append(ward)
     context.bot.send_message(update.effective_chat.id, ' '.join(list))

 start_handler = MessageHandler(Filters.text, start)
 dispahather.add_handler(start_handler)
 updater.start_polling()
 updater.idle()s