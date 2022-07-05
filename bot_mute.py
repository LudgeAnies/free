import logging
from aiogram import Bot, Dispatcher, executor, types

from database import Database
import param

logging.basicConfig(level=logging.INFO)

bot = Bot(token=param.TOKEN)
dp = Dispatcher(bot)
db = Database('base.db')


@dp.message_handler(commands=["mute"], commands_prefix='/')
async def mute_days_handler(message: types.Message):
    if str(message.from_user.id) == param.ADMIN_ID:
        if not message.reply_to_message:
            await message.reply('Эта команда должна быть ответом на сообщение!')
            return
        mute_day = int(message.text[6:])
        db.add_mute_days(message.reply_to_message.from_user.id, mute_day)
        # await message.bot.delete_message(param.CHAT_ID, message.message_id)
        await message.reply_to_message.reply(f'Пользователь был замучен на {mute_day} дней!')

@dp.message_handler(commands=["info"], commands_prefix='/')
async def info_mute(message: types.Message):
    if str(message.from_user.id) == param.ADMIN_ID:
        if not message.reply_to_message:
            await message.reply('Эта команда должна быть ответом на сообщение!')
            return
        if not db.mute_user(message.from_user.id):
            await message.reply_to_message.reply('У пользователя отсутствует мут.')
        if db.mute_user(message.from_user.id):
            mute = db.mute_user(message.reply_to_message.from_user.id)
            await message.reply_to_message.reply(f'Пользователь в муте на {mute} дней.')


@dp.message_handler()
async def mess_handler(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)

    if db.mute_user(message.from_user.id):
        await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

