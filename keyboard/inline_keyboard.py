from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


BTN_BACK_MENU = InlineKeyboardButton('btn_back_menu', callback_data='menu')
BTN_MENU = InlineKeyboardButton('btn_menu', callback_data='menu')

START = InlineKeyboardMarkup().add(BTN_MENU)
BACK_MENU = InlineKeyboardMarkup().add(BTN_BACK_MENU)



BTN_CONSULTATION = InlineKeyboardButton('btn_consultation' + b'\xF0\x9F\x93\x9D'.decode('utf-8'), callback_data='consultation')
BTN_SITUATION = InlineKeyboardButton(b'\xF0\x9F\x94\xB9'.decode('utf-8') + 'btn_situatiion', callback_data='situation')
BTN_SS = InlineKeyboardButton(b'\xF0\x9F\x94\xB9'.decode('utf-8') + 'Some link button', url='https://core.telegram.org/')
SS = InlineKeyboardMarkup().add(BTN_SS)

BTN_GUIDE = InlineKeyboardButton('btn_guide', callback_data='guide')
BTN_SHOP = InlineKeyboardButton('btn_shop', callback_data='shop')

BTN_BACK_CONS = InlineKeyboardButton('btn_back_cons', callback_data='consultation')
BTN_CANCEL_CONS = InlineKeyboardButton('btn_cancel_cons', callback_data='cancel_cons')
CANCEL_CONS = InlineKeyboardMarkup(row_width=2).add(BTN_CANCEL_CONS, BTN_MENU)


MENU = InlineKeyboardMarkup().add(BTN_SS).add(BTN_CONSULTATION).add(BTN_SITUATION) ###.add(BTN_GUIDE).add(BTN_SHOP)



BTN_SIGNUP = InlineKeyboardButton('Signup' + b'\xF0\x9F\x93\x9D'.decode('utf-8'), callback_data='signup')
SIGNUP = InlineKeyboardMarkup().add(BTN_SIGNUP) # interview

BTN_WICH_PROBLEMS = InlineKeyboardButton(b'\x31\xE2\x83\xA3'.decode('utf-8'), url='https://core.telegram.org/')

BTN_HOW_TO_ASK = InlineKeyboardButton(b'\x32\xE2\x83\xA3'.decode('utf-8'), callback_data='how_to_ask')
HOW_TO_ASK = InlineKeyboardMarkup(row_width=2).add(BTN_SIGNUP).add(BTN_MENU, BTN_BACK_CONS)

BTN_WHAT_GET = InlineKeyboardButton(b'\x33\xE2\x83\xA3'.decode('utf-8'), callback_data='what_get')
WHAT_GET = InlineKeyboardMarkup(row_width=2).add(BTN_SIGNUP).add(BTN_MENU, BTN_BACK_CONS)

BTN_HOW_IT_GOES = InlineKeyboardButton(b'\x34\xE2\x83\xA3'.decode('utf-8'), callback_data='how_it_goes')
HOW_IT_GOES = InlineKeyboardMarkup(row_width=2).add(BTN_SIGNUP).add(BTN_MENU, BTN_BACK_CONS)

BTN_MEETCOUNT = InlineKeyboardButton(b'\x35\xE2\x83\xA3'.decode('utf-8'), callback_data='meetcount')
MEETCOUNT = InlineKeyboardMarkup(row_width=2).add(BTN_SIGNUP).add(BTN_MENU, BTN_BACK_CONS)

BTN_PRICE = InlineKeyboardButton(b'\x36\xE2\x83\xA3'.decode('utf-8'), callback_data='price')
PRICE = InlineKeyboardMarkup(row_width=2).add(BTN_SIGNUP).add(BTN_MENU, BTN_BACK_CONS)

BTN_CONSTIME = InlineKeyboardButton(b'\x37\xE2\x83\xA3'.decode('utf-8'), callback_data='constime')
CONSTIME = InlineKeyboardMarkup(row_width=2).add(BTN_SIGNUP).add(BTN_MENU, BTN_BACK_CONS)

BTN_RULES = InlineKeyboardButton(b'\x39\xE2\x83\xA3'.decode('utf-8'), callback_data='rules')
RULES = InlineKeyboardMarkup(row_width=2).add(BTN_SIGNUP).add(BTN_MENU, BTN_BACK_CONS)

BTN_REVIEWS = InlineKeyboardButton(b'\x38\xE2\x83\xA3'.decode('utf-8'), callback_data='reviews')
REVIEWS = InlineKeyboardMarkup(row_width=2).add(BTN_REVIEWS).add(BTN_MENU, BTN_BACK_CONS)



BTN_SITUATION_DESCRIPTION = InlineKeyboardButton('situation_description_btn', url='https://core.telegram.org/')
SITUATION_DESCRIPTION = InlineKeyboardMarkup().add(BTN_MENU)
BTN_SITUATION_SEND = InlineKeyboardButton('send_situation_btn', callback_data='situation_send')
SITUATION_SEND = InlineKeyboardMarkup().add(BTN_MENU)
SITUATION = InlineKeyboardMarkup().add(BTN_SITUATION_DESCRIPTION).add(BTN_MENU)


GUIDE = InlineKeyboardMarkup().add(BTN_GUIDE)
SHOP = InlineKeyboardMarkup().add(BTN_SHOP)

CONSULTATION = InlineKeyboardMarkup(row_width=4).add(BTN_WICH_PROBLEMS,
BTN_HOW_TO_ASK, BTN_WHAT_GET, BTN_HOW_IT_GOES, BTN_MEETCOUNT, BTN_PRICE, BTN_CONSTIME, BTN_REVIEWS).add(BTN_SIGNUP).add(BTN_MENU)

