from telegram.ext import ApplicationBuilder

from config import TOKEN

from warnings import filterwarnings
from telegram.warnings import PTBUserWarning

filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)

application = ApplicationBuilder().token(TOKEN).build()