from aiogram import types, Dispatcher
from register_bot import bot, dp
from messages import messages
from keyboard import inline_keyboard
from aiogram.types.input_media import InputMedia, InputFile


# @dp.callback_query_handler(text='how_to_ask')
async def howtoask(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    with open('pictures/how_to_ask.jpg', 'rb') as p:
        await bot.send_photo(
            callback_query.from_user.id,
            photo=p,
            caption=messages.how_to_ask,
            reply_markup=inline_keyboard.HOW_TO_ASK)


# @dp.callback_query_handler(text='what_get')
async def what_get(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    with open('pictures/what_get.jpg', 'rb') as p:
        await bot.send_photo(
            callback_query.from_user.id,
            photo=p,
            caption=messages.what_get,
            reply_markup=inline_keyboard.WHAT_GET)


# @dp.callback_query_handler(text='how_it_goes')
async def howitgoes(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    with open('pictures/how_it_goes.jpg', 'rb') as p:
        await bot.send_photo(
            callback_query.from_user.id,
            photo=p,
            caption=messages.how_it_goes,
            reply_markup=inline_keyboard.HOW_IT_GOES)


# @dp.callback_query_handler(text='meetcount')
async def meetcount(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    with open('pictures/meetcount.jpg', 'rb') as p:
        await bot.send_photo(
            callback_query.from_user.id,
            photo=p,
            caption=messages.meetcount,
            reply_markup=inline_keyboard.MEETCOUNT)


# @dp.callback_query_handler(text='price')
async def price(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.price,
        reply_markup=inline_keyboard.PRICE)


# @dp.callback_query_handler(text='constime')
async def constime(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    with open('pictures/constime.jpg', 'rb') as p:
        await bot.send_photo(
            callback_query.from_user.id,
            photo=p,
            caption=messages.constime,
            reply_markup=inline_keyboard.CONSTIME)


# @dp.callback_query_handler(text='rules')
async def rules(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.rules,
        reply_markup=inline_keyboard.RULES)


# @dp.callback_query_handler(text='reviews')
async def reviews(callback_query: types.CallbackQuery):
    markup = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(b'\xE2\x97\x80'.decode('utf-8'), callback_data=f'prev:0'),
        types.InlineKeyboardButton('reviews', callback_data='null'),
        types.InlineKeyboardButton(b'\xE2\x96\xB6'.decode('utf-8'), callback_data=f'next:1'),
        types.InlineKeyboardButton('signup' + b'\xF0\x9F\x93\x9D'.decode('utf-8'), callback_data='signup'),
        inline_keyboard.BTN_BACK_CONS
    )
    with open('reviews/review_1.jpg', 'rb') as p:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_photo(
        callback_query.from_user.id,
        photo=p,
        reply_markup=markup)


# @dp.callback_query_handler(text_startswith='prev')
async def prev_page(call: types.CallbackQuery):
    await call.answer()
    data = int(call.data.split(":")[1]) - 1
    if data > -12:
        # rev = messages.reviews_list[data]
        markup = types.InlineKeyboardMarkup().add(
                types.InlineKeyboardButton(b'\xE2\x97\x80'.decode('utf-8'), callback_data=f'prev:{data}'),
                types.InlineKeyboardButton('reviews', callback_data='null'),
                types.InlineKeyboardButton(b'\xE2\x96\xB6'.decode('utf-8'), callback_data=f'next:{data}'),
                types.InlineKeyboardButton('signup' + b'\xF0\x9F\x93\x9D'.decode('utf-8'), callback_data='signup'),
                inline_keyboard.BTN_BACK_CONS
            )
        await call.message.edit_media(InputMedia(media=InputFile('reviews/review_{}.jpg'.format(abs(data)))),
        reply_markup=markup)
    else:
        data = 0
        # rev = messages.reviews_list[data]
        markup = types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton(b'\xE2\x97\x80'.decode('utf-8'), callback_data=f'prev:{data}'),
            types.InlineKeyboardButton('reviews', callback_data="null"),
            types.InlineKeyboardButton(b'\xE2\x96\xB6'.decode('utf-8'), callback_data=f'next:{data}'),
            types.InlineKeyboardButton('signup' + b'\xF0\x9F\x93\x9D'.decode('utf-8'), callback_data='signup'),
            inline_keyboard.BTN_BACK_CONS
        )
        await call.message.edit_media(InputMedia(media=InputFile('reviews/review_{}.jpg'.format(abs(data)))),
        reply_markup=markup)

# @dp.callback_query_handler(text_startswith='next')
async def next_page(call: types.CallbackQuery):
    await call.answer()
    data = int(call.data.split(":")[1]) + 1
    if data < 12:
        # rev = messages.reviews_list[data]
        markup = types.InlineKeyboardMarkup().add(
                types.InlineKeyboardButton(b'\xE2\x97\x80'.decode('utf-8'), callback_data=f'prev:{data}'),
                types.InlineKeyboardButton('reviews', callback_data='null'),
                types.InlineKeyboardButton(b'\xE2\x96\xB6'.decode('utf-8'), callback_data=f'next:{data}'),
                types.InlineKeyboardButton('signup' + b'\xF0\x9F\x93\x9D'.decode('utf-8'), callback_data='signup'),
                inline_keyboard.BTN_BACK_CONS
            )
        await call.message.edit_media(InputMedia(media=InputFile('reviews/review_{}.jpg'.format(abs(data)))),
        reply_markup=markup)
    else:
        data = 0
        # rev = messages.reviews_list[data]
        markup = types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton(b'\xE2\x97\x80'.decode('utf-8'), callback_data=f'prev:{data}'),
            types.InlineKeyboardButton('reviews', callback_data='null'),
            types.InlineKeyboardButton(b'\xE2\x96\xB6'.decode('utf-8'), callback_data=f'next:{data}'),
            types.InlineKeyboardButton('signup' + b'\xF0\x9F\x93\x9D'.decode('utf-8'), callback_data='signup'),
            inline_keyboard.BTN_BACK_CONS
        )
        await call.message.edit_media(InputMedia(media=InputFile('reviews/review_{}.jpg'.format(abs(data)))),
        reply_markup=markup)


def register_consultation_callbacks(dp:Dispatcher):
    dp.register_callback_query_handler(howtoask, text='how_to_ask')
    dp.register_callback_query_handler(what_get, text='what_get')
    dp.register_callback_query_handler(howitgoes, text='how_it_goes')
    dp.register_callback_query_handler(meetcount, text='meetcount')
    dp.register_callback_query_handler(price, text='price')
    dp.register_callback_query_handler(constime, text='constime')
    dp.register_callback_query_handler(rules, text='rules')
    dp.register_callback_query_handler(reviews, text='reviews')
    dp.register_callback_query_handler(prev_page, text_startswith='prev')
    dp.register_callback_query_handler(next_page, text_startswith='next')

