import asyncio

from aiogram import Bot, Dispatcher
from aiogram.dispatcher import router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import g4f

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = '6829297492:AAGAcsRcH0JsN46MpFj0VrW0dxJpG5FKmVk'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def gpt(request: str) -> str:
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": f'{request}'}],
            provider=g4f.Provider.GptGo,
        )
        return response
    except Exception as e:
        return str(e)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЗадай мне вопрос!')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и я пришлю тебе ответ на твой вопрос'
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"

@dp.message()
async def send_echo(message: Message):
    await bot.send_message(message.chat.id, 'Поиск ответа...')
    a = await gpt(message.text)
    await bot.send_message(message.chat.id, a)

if __name__ == '__main__':
    dp.run_polling(bot)
