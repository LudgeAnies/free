from datetime import datetime, timedelta
from aiogram import *
import logging

import param

bot = Bot(token=param.TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['мут', 'mute'], commands_prefix='./', is_chat_admin=True)
async def mute(message):
    name1 = message.from_user.get_mention(as_html=True)
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение!")
        return
    try:
        muteint = int(message.text.split()[1])
        mutetype = message.text.split()[2]
        comment = " ".join(message.text.split()[3:])
    except IndexError:
        await message.reply('Не хватает аргументов!\nПример:\n`/мут 1 ч причина`')
        return
    if mutetype == "ч" or mutetype == "часов" or mutetype == "час":
        dt = datetime.now() + timedelta(hours=muteint)
        timestamp = dt.timestamp()
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                       types.ChatPermissions(False), until_date=timestamp)
        await message.reply(
            f' | <b>Решение было принято:</b> {name1}\n | <b>Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | <b>Срок наказания:</b> {muteint} {mutetype}\n | <b>Причина:</b> {comment}',
            parse_mode='html')
    elif mutetype == "м" or mutetype == "минут" or mutetype == "минуты":
        dt = datetime.now() + timedelta(minutes=muteint)
        timestamp = dt.timestamp()
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                       types.ChatPermissions(False), until_date=timestamp)
        await message.reply(
            f' | <b>Решение было принято:</b> {name1}\n | <b>Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | <b>Срок наказания:</b> {muteint} {mutetype}\n | <b>Причина:</b> {comment}',
            parse_mode='html')
    elif mutetype == "д" or mutetype == "дней" or mutetype == "день":
        dt = datetime.now() + timedelta(days=muteint)
        timestamp = dt.timestamp()
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                       types.ChatPermissions(False), until_date=timestamp)
        await message.reply(
            f' | <b>Решение было принято:</b> {name1}\n | <b>Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | <b>Срок наказания:</b> {muteint} {mutetype}\n | <b>Причина:</b> {comment}',
            parse_mode='html')

if __name__ == '__main__':
    executor.start_polling(dp)
