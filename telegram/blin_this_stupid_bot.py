from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '6711414028:AAHyrrnZaBCrDreavj7E32uNaZWNxRzGqlI'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("start")

@dp.message_handler(commands=['test'])
async def send_welcome(message: types.Message):
   await bot.send_message(1292677678,"test")


@dp.message_handler()
async def echo(message: types.Message):
   print(message)
   id = message.from_id
   name = message.from_user.first_name
   text = "Привет "
   if message.text!="привет":
      await bot.send_message(id, "Иди на фик")
   if message.text=="привет":
      await bot.send_message(id, text+name)




if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)