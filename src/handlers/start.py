from telegram import Update
from telegram.ext import MessageHandler, ConversationHandler, filters, CallbackQueryHandler, ContextTypes, CommandHandler, InvalidCallbackData

from funcs.start import start

app_start_handler = [
    CommandHandler(['start'], start, filters=filters.ChatType.ALL)
]

