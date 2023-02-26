from aiogram import types, Dispatcher
from register_bot import bot, dp
from messages import messages
from keyboard import inline_keyboard

from aiogram.dispatcher import FSMContext

# @dp.message_handler(commands='start')
async def start(message: types.Message):
    with open('pictures/start_photo.jpg', 'rb') as photo:
        await message.answer_photo(photo=photo, caption=messages.start,
        reply_markup=inline_keyboard.START)


# @dp.message_handler(commands='menu')
async def menu(message: types.Message):
    await message.answer(messages.menu,
                            reply_markup=inline_keyboard.MENU)


# @dp.callback_query_handler(text='menu', state='*')
async def callback_menu(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.menu,
        reply_markup=inline_keyboard.MENU)
    await state.finish()


def register_common_handlers(dp:Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(menu, commands='menu')
    dp.register_callback_query_handler(callback_menu, text='menu', state='*')