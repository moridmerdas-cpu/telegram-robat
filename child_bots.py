from telegram.ext import Updater, MessageHandler, Filters
from config import CHILD_BOTS
import threading

def react(update, context):
    if update.channel_post:
        context.bot.send_message(
            chat_id=update.channel_post.chat_id,
            text="❤️",
            reply_to_message_id=update.channel_post.message_id
        )

def run_bot(bot):
    updater = Updater(bot["token"])
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.chat_type.channel, react))
    updater.start_polling()
    updater.idle()

def main():
    threads = []
    for bot in CHILD_BOTS:
        t = threading.Thread(target=run_bot, args=(bot,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()