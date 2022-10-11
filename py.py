from aiogram import Bot,executor,Dispatcher,types


TOKEN = '5557676933:AAFl9LpMWkhkrj1RQuRJ8bM21Cxq8zhqCcM'
bot = Bot(TOKEN)
dp = Dispatcher(bot)
@dp.message_handler()
async def main(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,skip_updates=False)