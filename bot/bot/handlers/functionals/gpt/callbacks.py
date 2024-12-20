from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from openai import OpenAI

from bot.states import GPTState
from bot import keyboards

callbacks_router = Router()


@callbacks_router.callback_query(F.data == 'question')
async def adaptation(callback: types.CallbackQuery, state: FSMContext, openai_client: OpenAI):
    await state.update_data(delete='delete')
    thread = openai_client.beta.threads.create()
    await state.update_data(thread_id=thread.id)
    await state.set_state(GPTState.gpt)
    await callback.message.delete()

    previous_message = await callback.message.answer_photo(
        photo=types.FSInputFile('./files/Заставка стартового экрана.png'),
        caption='Задайте вопрос\n'
             '\nПримеры:\n'
             '- Как собрать заказ?\n'
             '- Что делать со злым гостем?\n'
             '- Как повысить зарплату?\n'
             '\nБот помнит историю диалога, но если нужно начать новый, то закончи его сам, нажав кнопку "Закончить '
             'диалог"',
        reply_markup=keyboards.functionals.gpt.BACK_GPT_KEYBOARD
    )
    await state.update_data(previous_message_id=previous_message.message_id)
