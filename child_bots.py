from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from config import CHILD_BOTS
import asyncio

async def react(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        message_id = update.channel_post.message_id
        chat_id = update.channel_post.chat_id
        # استفاده از قابلیت جدید setMessageReaction
        await context.bot.send_reaction(chat_id=chat_id, message_id=message_id, emoji="❤️")

async def run_bot(bot_token):
    app = ApplicationBuilder().token(bot_token).build()
    app.add_handler(MessageHandler(filters.CHAT_TYPE_CHANNEL, react))
    await app.start()
    await app.updater.start_polling()
    await asyncio.Event().wait()  # نگه داشتن ربات

async def main():
    tasks = []
    for bot in CHILD_BOTS:
        tasks.append(run_bot(bot["token"]))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
