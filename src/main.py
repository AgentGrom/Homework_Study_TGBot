from telegram import Update
from telegram.ext import (
    MessageHandler, 
    filters
)

from app.app import application
from handlers.start import app_start_handler

application.add_handlers(app_start_handler)

application.run_polling(allowed_updates=Update.ALL_TYPES)