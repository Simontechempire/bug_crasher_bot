from telegram.ext import Application

from config import BOT_TOKEN
from database.db import init_db
from handlers.start import register as register_start
from handlers.help import register as register_help
from handlers.number import register as register_number
from handlers.group import register as register_group
from handlers.owner import register as register_owner


def main():
    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    register_start(app)
    register_help(app)
    register_number(app)
    register_group(app)
    register_owner(app)

    print("🤖 Bug Crasher Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()
