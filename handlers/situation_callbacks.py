from aiogram import types, Dispatcher
from register_bot import bot, dp
from messages import messages
from keyboard import inline_keyboard





# @dp.callback_query_handler(text='situation_description')
async def situation_description(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.situation_description,
        reply_markup=inline_keyboard.SITUATION_DESCRIPTION)


# @dp.callback_query_handler(text='situation_send')
async def situation_send(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.situation_send,
        reply_markup=inline_keyboard.SITUATION_SEND)



def register_callbacks_situation(dp:Dispatcher):
    dp.register_callback_query_handler(situation_description, text='situation_description')
    dp.register_callback_query_handler(situation_send, text='situation_send')