from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config

bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.reply_to_message(f'Hi, {msg.from_user.first_name}. Press 9')

#продумать логику рандомного ввода на разных языках. тут только цифры
@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == '9': #сделать или цифру буквами
       await msg.answer('Нет таких зарлат в Польше')
   else:
       await msg.answer('Error.')

# async def send_welcome(msg: types.Message):
#     if msg.reply_to_message is not None:
#         await msg.reply_to_message(f'Hi, {msg.from_user.first_name}. Press 9')
#     else:
#         await msg.reply('Reply to a message to use this command.')



if __name__ == '__main__':
   executor.start_polling(dp)