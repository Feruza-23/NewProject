import telebot
from telebot.types import Message
bot = telebot.TeleBot('8017345247:AAF0HNds9hSm5xHJbcvBhYnBFI2fu0eUkSM')

@bot.message_handler(commands=['start'])
def start_cmd(message: Message):
    bot.send_message(message.chat.id,'Привет! Я бот, который поможет вам узнать о глобальном потеплении. '
                     'Используйте /help_command для получения информации о командах бота.')

@bot.message_handler(commands=['help_command'])
def help_command(message: Message):
    bot.send_message(message.chat.id,'Используйте следующие команды:\n'
                              '/start - Начать взаимодействие с ботом\n'
                              '/info - Узнать о глобальном потеплении\n'
                              '/tips - Получить советы по его предотвращению\n'
                              '/resources - Полезные ресурсы\n'
                              '/quiz - Квиз на тему глобального потепления')

@bot.message_handler(commands=['info'])
def handle_info(message: Message):
    bot.send_message(message.chat.id, 'Глобальное потепление — это долгосрочное повышение средней температуры Земли. Основная причина — увеличение концентрации парниковых газов в атмосфере, таких как CO2 и метан.')

@bot.message_handler(commands=['tips'])
def handle_tips(message: Message):
    bot.send_message(message.chat.id, 'Вот несколько советов по борьбе с глобальным потеплением:\n'
                              '1. Сократите использование одноразового пластика.\n'
                              '2. Используйте общественный транспорт или велосипеды.\n'
                              '3. Энергосбережение в доме (например, выключение света).\n'
                              '4. Поддерживайте устойчивое сельское хозяйство и покупайте местные продукты.\n'
                              '5. Участвуйте в акциях по высадке деревьев и сохранению природы.')

@bot.message_handler(commands=['resources'])
def handle_resources(message: Message):
    bot.send_message(message.chat.id,'Вот несколько ресурсов для получения дополнительной информации:\n'
                              '1. [IPCC](https://www.ipcc.ch/) - Межправительственная группа экспертов по изменению климата.\n'
                              '2. [NASA Climate Change](https://climate.nasa.gov/) - Информация о климатических изменениях от NASA.\n'
                              '3. [WWF](https://www.worldwildlife.org/) - Всемирный фонд дикой природы.\n'
                              '4. https://www.un.org/ru/un75/climate-crisis-race-we-can-win - Статья ООН о глобальном потеплении. \n'
                              '5. https://www.un.org/ru/climatechange/science/causes-effects-climate-change - Статья ООН о причинах и последствиях глобального потепления.\n')

@bot.message_handler(commands=['quiz'])
def handle_quiz(message: Message):
    bot.send_message(message.chat.id, 'Проверьте свои знания, пройдя квиз на тему "Глобальное потепление" https://quizizz.com/admin/quiz/627bcf99fbb50f001d40fd67/%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5-%D0%BF%D0%BE%D1%82%D0%B5%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5')

bot.polling()
