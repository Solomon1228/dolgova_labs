import os
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
from random import choice
import dotenv
from aiogram.filters import CommandStart

dotenv.load_dotenv()
kb_buttons = [KeyboardButton(text = 'Дай расписание'), KeyboardButton(text = 'Сколько времени?'), KeyboardButton(text = "Дай смешную картинку")]
main_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[kb_buttons])


API_TOKEN = os.environ.get('TELEGRAM_TOKEN')


# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Я вас категорически приветствую", reply_markup=main_kb)


@dp.message()
async def echo(message: types.Message):
    if message.text == 'Дай расписание' :
        await message.answer('Отправляю расписание')
        pic = types.FSInputFile("images/raspisanie.png")
        await bot.send_photo(chat_id=message.chat.id, photo=pic)
       
    elif message.text == 'Сколько времени?' :
        time = datetime.now()
        m = f'Мне кажется: {time:%H:%M}' 
        await message.answer(m)
    elif message.text == 'Дай смешную картинку' :
        files = os.listdir("images")
        files.remove("raspisanie.png")
        pic = choice(files)
        await message.answer("Лови аптечку")
        picture = types.FSInputFile(os.path.join("images", pic))
        await bot.send_photo(chat_id=message.chat.id, photo = picture)       
    else:
        await message.answer('Я не разговариваю на человеческом')


if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot ,skip_updates = True))