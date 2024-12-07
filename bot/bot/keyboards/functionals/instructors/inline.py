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
    sub_topics = topic['subTopics']

    buttons = []


    for sub_topic in sub_topics:
        button = InlineKeyboardButton(text=sub_topic['name'], callback_data=f'topic_{sub_topic["id"]}')
        buttons.append([button])

    buttons.append([InlineKeyboardButton(text='Вернуться назад', callback_data='instructors')])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


INSTRUCTOR_TOPIC_BACK_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Вернуться назад', callback_data='instructors'),
        ]
    ]
)


