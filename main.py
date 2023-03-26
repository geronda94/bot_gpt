from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from aiogram.filters import Filter, Command, Text
import asyncio
import logging #импортируем библиотеку логирования
import aiohttp
import openai
from config import BOT_TOKEN, TOKEN, ADMIN, API_KEY



#Блок стартовых функций#########################
async def start_bot(bot: Bot): #функция срабатывает когда запускается сервер с ботом
    await bot.send_message(ADMIN, text='Бот запущен!')
async def stop_bot(bot: Bot):
    await bot.send_message(ADMIN, text='Бот остановлен')
async def get_start(message: Message, bot: Bot): #Функция срабатывает когда юзер дает команду /start
    await message.answer('Давай начнем!')


def req_openai(mes):
    openai.api_key = API_KEY
    prompt = str(mes)
    model = "text-davinci-003"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=4000,
        temperature=0.1,
        n=1,
        stop=None,
    )

    #print(response)
    return response.choices[0].text
   

async def echo(message: Message):   
    mes = req_openai(message.text)
    await message.reply(mes)



#Тело бота#####################################
async def start():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(name)s -(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.startup.register(start_bot) #Регистрируем хэндлер срабатывающий при запуске
    dp.shutdown.register(stop_bot)



    dp.message.register(get_start, Command(commands=['start'])) #Регистрируем хэндлер на команду /start
    dp.message.register(echo)




    try:
        #Начало сессии
        await dp.start_polling(bot)
    finally:
        #Закрываем сессию
        await bot.session.close()
###############################################


#Запускаем функцию Бота########################
if __name__ =="__main__":
    asyncio.run(start())
