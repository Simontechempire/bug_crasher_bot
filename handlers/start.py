from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from keyboards.main_menu import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to Bug Crasher Bot\n\n"
        "This is a real ban  system.\n\n"
        "Choose an operation below:",
        reply_markup=main_menu(),
    )


def register(app):
    app.add_handler(CommandHandler("start", start))
