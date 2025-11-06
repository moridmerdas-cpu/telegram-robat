from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config import MOTHER_TOKEN, CHILD_BOTS, OWNER_ID

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id != OWNER_ID:
        update.message.reply_text("فقط مدیر می‌تونه از این ربات استفاده کنه ❌")
        return

    buttons = [
        [InlineKeyboardButton(f"ربات فرعی {i+1}", url=f"https://t.me/{bot['username']}")]
        for i, bot in enumerate(CHILD_BOTS)
    ]
    markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text("ربات‌های فرعی:", reply_markup=markup)

def main():
    updater = Updater(MOTHER_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()