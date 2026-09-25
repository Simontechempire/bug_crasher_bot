from telegram import Update
from telegram.ext import CommandHandler, ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 HELP\n\n"
        "/start - Open main menu\n"
        "/ban <number> - Submit authentic ban request\n"
        "/unban <number> - Submit authentic unban request\n"
        "/ban_group <group> - Submit authentic group ban request\n"
        "/unban_group <group> - Submit authentic group unban request\n"
        "/pending - Owner pending requests\n\n"
        "All requests require owner approval."
    )


def register(app):
    app.add_handler(CommandHandler("help", help_command))
