import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.bot import DefaultBotProperties
import asyncpg
import keyboards

API_TOKEN = '7152751138:AAH5yM2oi6URy0UDzcI98AsJ_qZUyuWS5HI'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()

async def connect_db():
    return await asyncpg.connect(
        user='postgres',
        password='1425',
        database='postgres',
        host='localhost'
    )

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello Guys", reply_markup=keyboards.main_kb)

@dp.message()
async def echo(message: Message):
    if message.text:
        msg = message.text.lower()
        if msg == "maqola":
            await message.answer("Maqolangiz manzili", reply_markup=keyboards.links_kb)
        elif msg == "dissertatsiyalar":
            await message.answer("Dissertatsiyalar", reply_markup=keyboards.spec_kb)
        elif msg == "tezis":
            await message.answer("Tezislar ro'yxati", reply_markup=keyboards.tezis_kb)
        elif msg == "ortga":
            await message.answer("Bosh menyuga qaytdingiz", reply_markup=keyboards.main_kb)
    # Process standard text commands

    # Handle phone number
    elif message.contact:  # This checks if the message contains a contact
        phone_number = message.contact.phone_number
        user_id = message.from_user.id
        await save_phone_number(user_id, phone_number)
        await message.answer("Thank you! Your phone number has been saved.")

async def save_phone_number(user_id, phone_number):
    conn = await connect_db()
    try:
        # Insert or update the phone number
        await conn.execute('''
            INSERT INTO phone_numbers (user_id, phone_number)
            VALUES ($1, $2)
            ON CONFLICT (user_id) DO UPDATE 
            SET phone_number = EXCLUDED.phone_number;
        ''', user_id, phone_number)
    except Exception as e:
        print(f"An error occurred: {e}")  # Print error to console for debugging
    finally:
        await conn.close()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
