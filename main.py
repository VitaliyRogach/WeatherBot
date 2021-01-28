import logging
import config
from dbhundler import SQLighter
from aiogram import Bot, Dispatcher, executor, types
from wheather_parser import parser


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

"""Инициализация соединения с БД"""
db = SQLighter('db.db')

# Вывод условия при начале использования бот при команде START
@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.answer("Пиши '/' и увидишь команды. ")
    await message.answer_sticker(r'CAACAgIAAxkBAAEB0rFgEqgIZkOJjyimU-kH7-xnH3qAdAACYwIAAs3ASBgwJUq5vj4DRR4E')
# Команда активации подписки
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        # Если юзера нет в базе, добавляем его
        db.add_subscriber(message.from_user.id)
    else:
        # Если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(message.from_user.id, True)
    gt = parser()
    await message.answer("Здорова, Бандит! Получи прогноз!\n" + gt)






# Команда отписки
@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        # Если юзера нет в базе, добавляем его с неактивной подпиской
        db.add_subscriber(message.from_user.id, False)
        await message.answer("Ты и так не с нами!")
    else:
        # Если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(message.from_user.id, False)
        await message.answer("Отписан! Будешь скучать - заглядывай!")



# Запуск
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)