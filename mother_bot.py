from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import MOTHER_TOKEN, CHILD_BOTS, OWNER_ID

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != OWNER_ID:
        await update.message.reply_text("فقط مدیر می‌تونه از این ربات استفاده کنه ❌")
        return

    buttons = [
        [InlineKeyboardButton(f"ربات فرعی {i+1}", url=f"https://t.me/{bot['username']}")]
        for i, bot in enumerate(CHILD_BOTS)
    ]
    markup = InlineKeyboardMarkup(buttons)
    await update.message.reply_text("ربات‌های فرعی:", reply_markup=markup)

app = ApplicationBuilder().token(MOTHER_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
