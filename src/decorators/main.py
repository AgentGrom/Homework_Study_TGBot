from telegram import Message, Update

def privat_chat_check(func):
    async def wrapper(*args, **kwargs):
        update: Update = args[0]
        if update.callback_query: message = update.callback_query.message
        else:                     message = update.message
        # context: ContextTypes.DEFAULT_TYPE = args[1]

        if message.chat.type != 'private': return

        return await func(*args, **kwargs)
    return wrapper