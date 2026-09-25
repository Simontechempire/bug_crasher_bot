🤖 Bug Crasher Bot

A Telegram-based request and approval system for managing simulated WhatsApp-style account and group status changes.

«⚠️ Safety notice: This project is designed for testing and simulation. It does not automatically ban, unban, or mass-report real WhatsApp accounts or groups.»

✨ Features

- "/start" interactive menu
- Ban-number request
- Unban-number request
- Ban-group request
- Unban-group request
- Reason collection
- Owner approval workflow
- Approve / reject buttons
- Request IDs
- SQLite database
- Audit logging
- User notifications
- Owner-only controls
- Simulated target status changes

📁 Project Structure

bug_crasher_bot/
│
├── bot.py
├── config.py
├── requirements.txt
├── .env
│
├── handlers/
│   ├── start.py
│   ├── help.py
│   ├── number.py
│   ├── group.py
│   └── owner.py
│
├── services/
│   ├── ban_service.py
│   ├── unban_service.py
│   ├── report_service.py
│   └── approval_service.py
│
├── database/
│   ├── db.py
│   ├── models.py
│   └── repository.py
│
├── keyboards/
│   ├── main_menu.py
│   └── approval.py
│
├── utils/
│   ├── validation.py
│   └── logger.py
│
└── data/
    └── bot.db

⚙️ Requirements

- Python 3.10+
- Telegram Bot Token
- Telegram Owner ID

Install dependencies:

pip install -r requirements.txt

🔐 Configuration

Create ".env":

BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
OWNER_ID=YOUR_TELEGRAM_USER_ID
DATABASE_URL=sqlite:///data/bot.db

Never publish your bot token or commit ".env" to GitHub.

🚀 Start the Bot

python bot.py

Then open your Telegram bot and send:

/start

🧭 User Flow

Ban Number

/ban 234xxxxxxxx
        ↓
Reason?
        ↓
Create request
        ↓
Owner review
        ↓
Approve / Reject

Unban Number

/unban 234xxxxxxxx
        ↓
Reason?
        ↓
Create request
        ↓
Owner review
        ↓
Approve / Reject

Ban Group

/ban group
        ↓
Group identifier
        ↓
Reason?
        ↓
Owner review
        ↓
Approve / Reject

Unban Group

/unban group
        ↓
Group identifier
        ↓
Reason?
        ↓
Owner review
        ↓
Approve / Reject

🔐 Owner Approval

Every request is initially:

status = pending

The owner receives:

🔔 NEW REQUEST

Request: #1042
Type: NUMBER UNBAN
Target: 234xxxxxxxx

Reason:
This number can now use WhatsApp.

[✅ APPROVE] [❌ REJECT]

Approval changes the simulated target state and records the action in the audit log.

🗃️ Request States

pending
   │
   ├── approved
   │
   └── rejected

Target states:

active
banned

📊 Audit Logging

Important actions are recorded:

Request ID
User ID
Target
Action
Previous status
New status
Reviewer
Timestamp

This makes the system easier to debug and prevents silent status changes.

🛡️ Security

The bot should:

- Restrict owner commands to "OWNER_ID"
- Validate submitted identifiers
- Rate-limit requests
- Prevent duplicate pending requests
- Store secrets in environment variables
- Log administrative actions
- Never expose the bot token
- Use parameterized database queries

🧪 Testing

The project should use a real target database.

Example:

Target: 234xxxxxxxx
Type: number
Status: banned

After an approved unban request:

Target: 234xxxxxxxx
Type: number
Status: active

 real WhatsApp enforcement is performed.

📜 License

Use this project only for authorized development, , and educational purposes.
