from telegram import Message, Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: Message = update.message

    telegram_id = message.chat.id
    await message.reply_text(
        f"Привет, {telegram_id}"
    )
    return 
    
    