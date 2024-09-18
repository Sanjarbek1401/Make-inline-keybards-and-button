import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.bot import DefaultBotProperties
import keyboards

API_TOKEN = '7152751138:AAH5yM2oi6URy0UDzcI98AsJ_qZUyuWS5HI'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello Guys", reply_markup=keyboards.main_kb)


@dp.message()
async def echo(message: Message):
    msg = message.text.lower()
    # Process standard text commands
    if msg == "maqola":
        await message.answer("Maqolangiz manzili", reply_markup=keyboards.links_kb)
    elif msg == "dissertatsiyalar":
        await message.answer("Dissertatsiyalar", reply_markup=keyboards.spec_kb)
    elif msg == "tezis":
        await message.answer("Tezislar ro'yxati", reply_markup=keyboards.tezis_kb)
    elif msg == "ortga":
        await message.answer("Bosh menyuga qaytdingiz", reply_markup=keyboards.main_kb)

    # Handle phone number
    elif message.contact:  # This checks if the message contains a contact
        phone_number = message.contact.phone_number
        user_id = message.from_user.id
        save_phone_number(user_id, phone_number)
        await message.answer("Thank you! Your phone number has been saved.")


def save_phone_number(user_id, phone_number):
    # Saving phone number to a text file for simplicity
    with open('phone_numbers.txt', 'a') as f:
        f.write(f'User ID: {user_id}, Phone Number: {phone_number}\n')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
