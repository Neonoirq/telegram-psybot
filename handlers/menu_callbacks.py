from aiogram import types, Dispatcher
from register_bot import bot, dp
from messages import messages
from keyboard import inline_keyboard


# @dp.callback_query_handler(text='consultation')
async def consultation(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    with open('pictures/consultation.png', 'rb') as photo:
        await bot.send_photo(
        callback_query.from_user.id,
        photo=photo,
        caption='\n'.join(messages.consultation_list),
        reply_markup=inline_keyboard.CONSULTATION)


# @dp.callback_query_handler(text='situation')
async def situation(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    with open('pictures/situation.jpg', 'rb') as p:
        await bot.send_photo(
            callback_query.from_user.id,
            photo=p,
            caption=messages.situation,
            reply_markup=inline_keyboard.SITUATION)

# @dp.callback_query_handler(text='ss')
async def ss(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.sn,
        reply_markup=inline_keyboard.BACK_MENU)


# @dp.callback_query_handler(text='shop')
async def shop(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.shop,
        reply_markup=inline_keyboard.BACK_MENU)


# @dp.callback_query_handler(text='guide')
async def guide(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.guide,
        reply_markup=inline_keyboard.BACK_MENU)


def register_menu_callbacks(dp:Dispatcher):
    dp.register_callback_query_handler(consultation, text='consultation')
    dp.register_callback_query_handler(situation, text='situation')
    dp.register_callback_query_handler(ss, text='ss')
    dp.register_callback_query_handler(shop, text='shop')
    dp.register_callback_query_handler(guide, text='guide')