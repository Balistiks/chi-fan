import time

from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from openai import OpenAI

from bot.misc.configuration import conf
from bot.states import GPTState
from bot import keyboards

messages_router = Router()


def wait_on_run(run, thread_id, openai_client: OpenAI):
    while run.status == "queued" or run.status == "in_progress":
        run = openai_client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run


@messages_router.message(GPTState.gpt)
async def gpt(message: types.Message, state: FSMContext, openai_client: OpenAI):
    await state.update_data(delete='not delete')
    data = await state.get_data()

    if 'previous_message_id' in data:
        try:
            await message.bot.edit_message_reply_markup(
                chat_id=message.chat.id,
                message_id=data['previous_message_id'],
                reply_markup=None
            )
        except Exception:
            pass

    answer_message = await message.answer('Загрузка 🔄')
    await message.bot.send_chat_action(message.chat.id, "typing")

    gpt_message = openai_client.beta.threads.messages.create(
        thread_id=data['thread_id'],
        role='user',
        content=message.text
    )

    run = openai_client.beta.threads.runs.create(
        thread_id=data['thread_id'],
        assistant_id=conf.openai.assistant_id,
    )

    wait_on_run(run, data['thread_id'], openai_client)

    answers = openai_client.beta.threads.messages.list(
        thread_id=data['thread_id'], order="asc", after=gpt_message.id
    )

    await answer_message.delete()

    answer_message = await message.answer(
        answers.data[0].content[0].text.value,
        reply_markup=keyboards.functionals.gpt.END_GPT_KEYBOARD
    )

    await state.update_data(previous_message_id=answer_message.message_id)

