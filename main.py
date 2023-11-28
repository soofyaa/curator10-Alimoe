import telebot
bot = telebot.TeleBot('6880175405:AAE9GoGvOje2VcPjhxEpcBeEdaZrXQ0f71g')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Добро пожаловать!', parse_mode='Markdown')

@bot.message_handler(commands=['token'])
def main(message):
    answer = '1. Открываем в телеграмме [BotFather](https://t.me/BotFather) и нажимаем start/начать\n'
    answer += '2. Выбираем команду _newbot_\n'
    answer += '3. Вводим любое название для бота. Потом вводим никнейм бота на английском слитно, которое обязательно заканчивается на слово *bot*\n'
    answer += '4. Придёт сообщение, где после API будет находится наш токен.'
    bot.send_message(message.chat.id, answer, parse_mode='Markdown')

@bot.message_handler(commands=['pers'])
def main(message):
    answer = '1. В [BotFather](https://t.me/BotFather) выбираем своего бота\n'
    answer += '2. Нажимаем кнопку _Edit Bot_\n'
    answer += '*Edit Name* - изменить имя\n'
    answer += '*Edit Description* - изменить сообщение на главной странице\n'
    answer += '*Edit About* - изменить описание\n'
    answer += '*Edit Botpic* - изменить аватарку\n'
    bot.send_message(message.chat.id, answer, parse_mode='Markdown')

bot.infinity_polling()