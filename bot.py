import telebot
from telebot import types

# Все, что нужно:
token = "1789258594:AAE3c_ejo50eoqVjHpxn7pJf4FOBk9S0_78" # токен основного бота
site = "https://qiwi.com/n/WHITERESELLER" # Cсылка оплаты(в конце ссылки пишите ваш ник QIWI)
channel = "https://t.me/joinchat/7v58kitS7oEwY2Y" # ИНФ канал
pod = "@THACKQ" # Аккаунт поддержки
admkanal= -337841013 # Айди админ канала

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def repeat_all_messages(message):
  bot.send_message(admkanal, f"@{message.chat.username} \n👋Написал: {message.text}")
  keyboard = types.InlineKeyboardMarkup()
  button1 = types.InlineKeyboardButton(text="✨Москва", callback_data="button1")
  button2 = types.InlineKeyboardButton(text="✨Воронеж", callback_data="button2")
  button3 = types.InlineKeyboardButton(text="✨Норильск", callback_data="button3")
  button4 = types.InlineKeyboardButton(text="✨Томск", callback_data="button4")
  button5 = types.InlineKeyboardButton(text="✨Краснодар", callback_data="button5")
  button6 = types.InlineKeyboardButton(text="✨Красноярск", callback_data="button6")
  button7 = types.InlineKeyboardButton(text="Санкт-Петербург", callback_data="button7")
  button8 = types.InlineKeyboardButton(text="Улан-Удэ", callback_data="button8")
  button9 = types.InlineKeyboardButton(text="Бийск", callback_data="button9")
  button10 = types.InlineKeyboardButton(text="Борисоглебцк", callback_data="button10")
  button11 = types.InlineKeyboardButton(text="Пермь", callback_data="button11")
  button12 = types.InlineKeyboardButton(text="Екатеринбург", callback_data="button12")
  button13 = types.InlineKeyboardButton(text="Сургут", callback_data="button13")
  button14 = types.InlineKeyboardButton(text="Сочи", callback_data="button14")
  button15 = types.InlineKeyboardButton(text="Ханты-Мансийский", callback_data="button15")
  button16 = types.InlineKeyboardButton(text="Абакан", callback_data="button16")
  button17 = types.InlineKeyboardButton(text="Оренбург", callback_data="button17")
  button18 = types.InlineKeyboardButton(text="Нижний Новгород", callback_data="button18")
  keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, button17, button18)
  bot.send_message(message.chat.id, "🛍Добро пожаловать в наш магазин.\nℹ️ИНФ-канал: "+str(channel)+"\n⚙️Поддержка: "+str(pod)+"\n☘️Пожалуйста, выберите город:", reply_markup=keyboard)

def button(message, city):
  keyboard1 = types.InlineKeyboardMarkup()
  button1 = types.InlineKeyboardButton(text="🈲HQD", callback_data="blue")
  button2 = types.InlineKeyboardButton(text="🈯JUUL", callback_data="red")
  bot.send_message(admkanal, f"@{message.chat.username} \n🏙Выбрал город: {city}")
  keyboard1.add(button1)
  keyboard1.add(button2)
  bot.send_message(message.chat.id, "✅Вы выбрали город "+str(city)+".\n☘️Теперь выберите товар:", reply_markup=keyboard1)

def blue(message, name):
  keyboard2 = types.InlineKeyboardMarkup()
  button1 = types.InlineKeyboardButton(text="HQD Cuvie - 300р", callback_data="b3")
  button2 = types.InlineKeyboardButton(text="HQD MAXIM - 230р", callback_data="b5")
  button3 = types.InlineKeyboardButton(text="HQD Stark - 270р", callback_data="b1")
  button4 = types.InlineKeyboardButton(text="HQD V2 - 245", callback_data="b2")
  bot.send_message(admkanal, f"@{message.chat.username} \n🛍Выбрал товар: {name}")
  keyboard2.add(button1)
  keyboard2.add(button2)
  keyboard2.add(button3)
  keyboard2.add(button4)
  bot.send_message(message.chat.id, "✅Вы выбрали "+str(name)+".\n☘️Теперь выберите HQD:", reply_markup=keyboard2)

def red(message, name):
  keyboard2 = types.InlineKeyboardMarkup()
  button1 = types.InlineKeyboardButton(text="Juul Labs JUUL (8W, 200 mAh) - 599р", callback_data="r3")
  button2 = types.InlineKeyboardButton(text="JUUL Pods - Mint - 599р", callback_data="r6")
  button3 = types.InlineKeyboardButton(text="Набор Juul Labs JUUL (8W, 200 mAh) - 999р", callback_data="r1")
  bot.send_message(admkanal, f"@{message.chat.username} \n🛍Выбрал товар: {name}")
  keyboard2.add(button1)
  keyboard2.add(button2)
  keyboard2.add(button3)
  bot.send_message(message.chat.id, "✅Вы выбрали "+str(name)+".\n☘️Теперь выберите JUUL:", reply_markup=keyboard2)

def buy(message):
  keyboard = types.InlineKeyboardMarkup()
  button1 = types.InlineKeyboardButton(text="Оплатить сейчас",url=site, callback_data="by")
  keyboard.add(button1)
  bot.send_message(message.chat.id, "✅Для оплаты нажмите на кнопку:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  message = call.message
  if call.message:
   if call.data == "button1":
      button(call.message, "Москва")
   elif call.data == "button2":
      button(call.message, "Воронеж")
   elif call.data == "button3":
      button(call.message, "Норильск")
   elif call.data == "button4":
      button(call.message, "Томск")
   elif call.data == "button5":
      button(call.message, "Краснодар")
   elif call.data == "button6":
      button(call.message, "Красноярск")
   elif call.data == "button7":
      button(call.message, "Санкт-Петербург")
   elif call.data == "button8":
      button(call.message, "Улан-Удэ")
   elif call.data == "button9":
      button(call.message, "Бийск")
   elif call.data == "button10":
      button(call.message, "Борисоглебцк")
   elif call.data == "button11":
        button(call.message, "Пермь")
   elif call.data == "button12":
      button(call.message, "Екатеринбург")
   elif call.data == "button13":
      button(call.message, "Сургут")
   elif call.data == "button14":
      button(call.message, "Сочи")
   elif call.data == "button15":
      button(call.message, "Ханты-Мансийский")
   elif call.data == "button16":
      button(call.message, "Абакан")
   elif call.data == "button17":
      button(call.message, "Оренбург")
   elif call.data == "button18":
      button(call.message, "Нижний Новгород")
   elif call.data == "blue":
      blue(call.message, "🈲HQD")
   elif call.data == "red":
      red(call.message, "🈯JUUL")
   elif call.data == "b3":
      bot.send_message(admkanal, f"@{message.chat.username} \n💸Оплачивает: HQD Cuvie - 300р")
      bot.send_message(message.chat.id, "Оплата-QIWI\nВы выбрали: HQD Cuvie\nК оплате: 300р.\nКоментарий: "+str(message.chat.id))
      buy(message)
   elif call.data == "b5":
      bot.send_message(admkanal, f"@{message.chat.username} \n💸Оплачивает: HQD MAXIM - 230р")
      bot.send_message(message.chat.id, "Оплата-QIWI\nВы выбрали: HQD MAXIM\nК оплате: 230р.\nКоментарий: "+str(message.chat.id))
      buy(message)
   elif call.data == "b1":
      bot.send_message(admkanal, f"@{message.chat.username} \n💸Оплачивает: HQD Stark - 270р")
      bot.send_message(message.chat.id, "Оплата-QIWI\nВы выбрали: HQD Stark\nК оплате: 350р.\nКоментарий: "+str(message.chat.id))
      buy(message)
   elif call.data == "b2":
      bot.send_message(admkanal, f"@{message.chat.username} \n💸Оплачивает: HQD V2 - 245р")
      bot.send_message(message.chat.id, "Оплата-QIWI\nВы выбрали: HQD V2\nК оплате: 245р.\nКоментарий: "+str(message.chat.id))
      buy(message)
   elif call.data == "r3":
      bot.send_message(admkanal, f"@{message.chat.username} \n💸Оплачивает: Juul Labs JUUL (8W, 200 mAh) - 599р")
      bot.send_message(message.chat.id, "Оплата-QIWI\nВы выбрали: Juul Labs JUUL (8W, 200 mAh)\nК оплате: 599р.\nКоментарий: "+str(message.chat.id))
      buy(message)
   elif call.data == "r6":
      bot.send_message(admkanal, f"@{message.chat.username} \n💸Оплачивает: JUUL Pods - Mint - 600р")
      bot.send_message(message.chat.id, "Оплата-QIWI\nВы выбрали: JUUL Pods - Mint\nК оплате: 600р.\nКоментарий: "+str(message.chat.id))
      buy(message)
   elif call.data == "r1":
      bot.send_message(admkanal, f"@{message.chat.username} \n💸Оплачивает: Набор Juul Labs JUUL (8W, 200 mAh) - 999р")
      bot.send_message(message.chat.id, "Оплата-QIWI\nВы выбрали: Набор Juul Labs JUUL (8W, 200 mAh)\nК оплате: 999р.\nКоментарий: "+str(message.chat.id))
      buy(message)
@bot.message_handler(content_types=['text'])
def echo_all(message):
      bot.send_message(admkanal, f"@{message.chat.username} \n👋Написал: {message.text}")
      bot.send_message(message.chat.id, "Вы что-то делаете не так, пожалуйста напишите - /start")

while True:
  bot.polling(none_stop=True)