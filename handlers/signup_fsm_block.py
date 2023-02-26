from aiogram import types, Dispatcher
from register_bot import bot, dp
from messages import messages
from keyboard import inline_keyboard

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from my_email import send_email



class Form(StatesGroup):
    name = State()
    question = State()
    description = State()
    phone_number = State()
    messenger = State()
    date = State()
    finish = State()


# @dp.callback_query_handler(text='signup')
async def callback_signup(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.signup
        )
    await bot.send_message(
            callback_query.from_user.id,
            text=messages.ask_name,
            reply_markup=inline_keyboard.CANCEL_CONS
            )
    await Form.name.set()


# @dp.callback_query_handler(text='cancel_cons', state='*')
async def callback_cansel_cons(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    with open('pictures/consultation.png', 'rb') as photo:
        await bot.send_photo(
        callback_query.from_user.id,
        photo=photo,
        caption='\n'.join(messages.consultation_list),
        reply_markup=inline_keyboard.CONSULTATION)

    await state.finish()


# @dp.message_handler(commands=['signup'])
async def get_name(message: types.Message):
    await message.answer(messages.signup)
    await message.answer(messages.ask_name, reply_markup=inline_keyboard.CANCEL_CONS)
    await Form.name.set()


# @dp.message_handler(state=Form.name)
async def get_question(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    buttons = [
    types.InlineKeyboardButton(str(i), callback_data='btn_' + str(i)) for i in range(1, 13)
    ]
    button_next = types.InlineKeyboardButton('Next', callback_data='btn_next')
    all_btn = types.InlineKeyboardMarkup(row_width=6).add(*buttons).add(button_next)
    async with state.proxy() as data:
        data['question'] = []
    await message.answer(messages.ask_question + '\n' * 2 +
    '\n'.join(messages.ask_question_list), reply_markup=all_btn)
    await Form.next()


# @dp.message_handler(state=Form.question)
async def get_description(message: types.Message, state: FSMContext):
    if message.text not in messages.ask_question_list:
        await message.answer("Choose situation using buttons, please")
        return
    await state.update_data(question=message.text.lower())
    await state.set_state(Form.question.state)
    await message.answer(messages.ask_description)
    await Form.next()


# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'), state=Form.question)
async def get_callback_question(callback_query: types.CallbackQuery, state: FSMContext):
    que = callback_query.data
    que_num = que.split('_')[1]
    if que == 'btn_next':
        await bot.send_message(callback_query.from_user.id, text=messages.ask_description)
        await Form.next()
    async with state.proxy() as data:
        if len(data['question']) < 4 and que_num != 'next':
            data['question'].append(messages.ask_question_dict[que_num])
            # await bot.send_message(
            #     callback_query.from_user.id,
            #     text=f'Пункт добавлен!')
        elif len(data['question']) == 4 and que_num != 'next':
            await bot.send_message(
            callback_query.from_user.id,
            text='Press "Next" button to continue')
    await bot.answer_callback_query(callback_query.id)


# @dp.message_handler(state=Form.description)
async def get_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer(messages.ask_phone_number)
    await Form.next()


# @dp.message_handler(state=Form.phone_number)
async def get_messenger(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    buttons = [
    types.InlineKeyboardButton('Telegram', callback_data='mes_tg'),
    types.InlineKeyboardButton('WhatsApp', callback_data='mes_ws')
    ]
    all_btn = types.InlineKeyboardMarkup(row_width=2).add(*buttons)
    await message.answer(messages.ask_messenger, reply_markup=all_btn)
    await Form.next()


# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('mes'), state=Form.messenger)
async def get_callback_messenger(callback_query: types.CallbackQuery, state: FSMContext):
    buttons = [
        types.InlineKeyboardButton('Fr: с 10 до 12', callback_data='date_mon1'),
        types.InlineKeyboardButton('Md: с 10 до 12', callback_data='date_fr1'),
        types.InlineKeyboardButton('Fr: с 12 до 15', callback_data='date_mon2'),
        types.InlineKeyboardButton('Md: с 12 до 15', callback_data='date_fr2'),
        types.InlineKeyboardButton('Fr: с 15 до 18', callback_data='date_mon3'),
        types.InlineKeyboardButton('Md: с 15 до 18', callback_data='date_fr3'),
        types.InlineKeyboardButton('Fr: с 18 до 20', callback_data='date_mon4'),
        types.InlineKeyboardButton('Md: с 18 до 20', callback_data='date_fr4')
    ]
    all_btn = types.InlineKeyboardMarkup(row_width=2).add(*buttons)
    mes = callback_query.data
    mes_name = mes.split('_')[1]
    if mes_name == 'tg':
        async with state.proxy() as data:
            data['messenger'] = "Telegram"
        # await bot.send_message(callback_query.from_user.id, text='Telegram')
        await bot.send_message(callback_query.from_user.id, text=messages.ask_date, reply_markup=all_btn)
        await bot.answer_callback_query(callback_query.id)
        await Form.next()
    elif mes_name == 'ws':
        async with state.proxy() as data:
            data['messenger'] = "WhatsApp"
        # await bot.send_message(callback_query.from_user.id, text='WhatsUp')
        await bot.send_message(callback_query.from_user.id, text=messages.ask_date, reply_markup=all_btn)
        await bot.answer_callback_query(callback_query.id)
        await Form.next()
    #await bot.answer_callback_query(callback_query.id)


# @dp.message_handler(state=Form.messenger)
async def get_messenger_err(message: types.Message, state: FSMContext):
    if message.text not in messages.ask_messenger_list:
        await message.answer("messenger")
        return
    await state.update_data(messenger=message.text)
    await message.answer(messages.ask_date)
    await Form.next()


# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('date'), state=Form.date)
async def get_callback_final_data(callback_query: types.CallbackQuery, state: FSMContext):
    #await state.update_data(date=message.text)
    day = callback_query.data
    day_time = day.split('_')[1]
    async with state.proxy() as data:
        data['date'] = messages.ask_date_dict[day_time]
    buttons = [
    types.InlineKeyboardButton('Send', callback_data='fin_send'),
    types.InlineKeyboardButton('Try again', callback_data='fin_again')
    ]
    all_btn = types.InlineKeyboardMarkup(row_width=1).add(*buttons)
    data = await state.get_data()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                    text=f"<b>Name:</b> <em>{data['name']}</em>\n"
                         f"<b>Question list:</b> <em>{', '.join(data['question'])}</em>\n"
                         f"<b>Description:</b> <em>{data['description']}</em>\n"
                         f"<b>Phone number:</b> <em>{data['phone_number']}</em>\n"
                         f"<b>Messenger:</b> <em>{data['messenger']}</em>\n"
                         f"<b>Time:</b> <em>{data['date']}</em>\n"
                         f"{messages.ask_finish}",
                         reply_markup=all_btn
                         )


# @dp.message_handler(state=Form.date)
async def get_date(message: types.Message, state: FSMContext):
    if message.text not in messages.ask_date_dict:
        await message.answer("Choose time using buttons, please")
        return
    await state.update_data(messenger=message.text)
    await message.answer(messages.ask_date)
    await Form.next()


# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('fin'), state=Form.date)
async def get_callback_restart(callback_query: types.CallbackQuery, state: FSMContext):
    fin = callback_query.data
    fin_end = fin.split('_')[1]
    if fin_end == 'again':
        await bot.send_message(
        callback_query.from_user.id,
        text=messages.ask_name,
        reply_markup=inline_keyboard.CANCEL_CONS
        )
        await Form.name.set()
    elif fin_end == 'send':
        data = await state.get_data()
        list_for_email = ['Name:' + data['name'],
                          'Question list:' + ' / '.join(data['question']),
                          'Description:' + data['description'],
                          'Phone number or Telegram:' + data['phone_number'],
                          'Messenger:' + data['messenger'],
                          'Date:' + data['date']]
        message_for_email = '\n'.join(list_for_email)
        send_email.send_email(message_for_email)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text='You have successfully signed up for a consultation',
        reply_markup=inline_keyboard.START)
        await state.finish()


def register_signup_fsm_block(dp:Dispatcher):
    dp.register_callback_query_handler(callback_signup, text='signup')
    dp.register_callback_query_handler(callback_cansel_cons, text='cancel_cons', state='*')
    dp.register_message_handler(get_name, text='signup')
    dp.register_message_handler(get_question, state=Form.name)
    dp.register_message_handler(get_description, state=Form.question)
    dp.register_callback_query_handler(get_callback_question, lambda c: c.data and c.data.startswith('btn'), state=Form.question)
    dp.register_message_handler(get_phone_number, state=Form.description)
    dp.register_message_handler(get_messenger, state=Form.phone_number)
    dp.register_callback_query_handler(get_callback_messenger, lambda c: c.data and c.data.startswith('mes'), state=Form.messenger)
    dp.register_message_handler(get_messenger_err, state=Form.messenger)
    dp.register_callback_query_handler(get_callback_final_data, lambda c: c.data and c.data.startswith('date'), state=Form.date)
    dp.register_message_handler(get_date, state=Form.date)
    dp.register_callback_query_handler(get_callback_restart, lambda c: c.data and c.data.startswith('fin'), state=Form.date)
