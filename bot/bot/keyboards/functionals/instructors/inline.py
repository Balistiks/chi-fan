from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.services import topics_service


async def instructor_keyboard() -> InlineKeyboardMarkup:
    topics = await topics_service.get_all()
    buttons = []

    for topic in topics:
        button = InlineKeyboardButton(text=topic['name'], callback_data=f'topic_{topic["id"]}')
        buttons.append([button])

    buttons.append([InlineKeyboardButton(text='Вернуться в главное меню', callback_data='main_menu')])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


async def instructor_topic_keyboard(topic_id: int) -> InlineKeyboardMarkup:
    topic = await topics_service.get_by_id(topic_id)
    parent_id = topic['parentId']
    callback_data = f'topic_{parent_id}'
    if parent_id == None:
        callback_data = 'instructors'
    sub_topics = topic['subTopics']

    buttons = []


    for sub_topic in sub_topics:
        button = InlineKeyboardButton(text=sub_topic['name'], callback_data=f'topic_{sub_topic["id"]}')
        buttons.append([button])
    buttons.append([InlineKeyboardButton(text='Вернуться назад', callback_data=f'{callback_data}')])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


async def instructor_topic_menu_keyboard(topic_id: int, current_page: int,) -> InlineKeyboardMarkup:
    topic = await topics_service.get_by_id(topic_id)
    parent_id = topic['parentId']
    parent = await topics_service.get_by_id(parent_id)
    text = topic['text']
    text_parts = text.split('#')
    number_pages = len(text_parts)
    # topic_id = parent['subTopics'][current_page - 1]['id']
    if topic['file']:
        file_topic_id = topic['file']['id']
    else:
        file_topic_id = None

    buttons = []

    if file_topic_id:
        buttons.append([InlineKeyboardButton(text='Посмотреть в общем файле', callback_data=f'topic-file_{file_topic_id}_{topic_id}')])

    buttons.append([InlineKeyboardButton(text='Вернуться назад', callback_data=f'topic_{parent_id}')])

    prev_callback_data = f'topic_{topic_id}_prev_page' if current_page + 1 > 1 else '#'
    next_callback_data = f'topic_{topic_id}_next_page' if current_page + 1 < number_pages else '#'
    if len(topic['subTopics']):
        navigation_buttons = []
    else:
        navigation_buttons = [
            InlineKeyboardButton(text='⬅️', callback_data=prev_callback_data),
            InlineKeyboardButton(text=f'{current_page + 1}/{number_pages}', callback_data='#'),
            InlineKeyboardButton(text='➡️', callback_data=next_callback_data)
        ]

    buttons.append(navigation_buttons)

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


async def instructor_topic_back_keyboard(topic_id: int) -> InlineKeyboardMarkup:
    buttons = []

    buttons.append([InlineKeyboardButton(text='Вернуться назад', callback_data=f'topic_{topic_id}')])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


INSTRUCTOR_TOPIC_BACK_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Вернуться назад', callback_data='instructors'),
        ]
    ]
)


