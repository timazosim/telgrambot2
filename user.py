from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.chat_states import ChatStates
from services.dialog_manager import dialog_manager
from services.gpt_api import ask_gpt

router = Router()

@router.message(F.text == "/start")
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Привіт! Я GPT-бот. Напиши щось.")
    await state.set_state(ChatStates.chatting)

@router.message(F.text == "/reset")
async def cmd_reset(message: Message, state: FSMContext):
    dialog_manager.clear_history(message.from_user.id)
    await message.answer("Контекст очищено.")
    await state.set_state(ChatStates.chatting)

@router.message(ChatStates.chatting)
async def handle_message(message: Message, state: FSMContext):
    user_id = message.from_user.id
    dialog_manager.add_message(user_id, "user", message.text)

    try:
        reply = await ask_gpt(dialog_manager.get_history(user_id))
    except Exception as e:
        await message.answer("Помилка при зверненні до GPT.")
        return

    dialog_manager.add_message(user_id, "assistant", reply)
    await message.answer(reply)
