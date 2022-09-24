from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from modules.config import BOT_USERNAME

HELP_TEXT = """
ʜᴇʟʟᴏ [{}](tg://user?id={})
ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ɴᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴀɴᴅ ɴᴏ ʟᴀɢ ɪssᴜᴇ ᴡɪᴛʜ ʙᴇsᴛ sᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs
ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ [𝐊𝐋𝐘 ༱ 𝐇𝐀𝐍𝐃𝐁𝐄𝐀 🇦🇱](https://t.me/Klyuserbot)...
━━━━━━━━━━━━━━━━━━━**"""


@Client.on_callback_query(filters.regex("home"))
async def home(_, query: CallbackQuery):
    await query.edit_message_text(f"{HELP_TEXT}".format(query.message.chat.first_name, query.message.chat.id),
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ Tambahkan Saya Ke Group Anda ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("🫂 sᴜᴘᴘᴏʀᴛ", url="https://t.me/TechQuardSupport"),
            InlineKeyboardButton("📣 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/TechQuard")
        ],
        [
            InlineKeyboardButton("🧰 ᴄᴏᴍᴍᴀɴᴅs", url="https://telegra.ph/Dim-COMMAND-09-23-3"),
            InlineKeyboardButton("⚕️ ᴍᴏʀᴇ ɪɴғᴏ", callback_data="moreinfo")
        ]
   
     ]
  ),
)






@Client.on_callback_query(filters.regex("moreinfo"))
async def others(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʜᴇʏᴀ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

Dim Musik untuk Telegram :""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗯️ ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/suportsipuserbot"),
                    InlineKeyboardButton(
                        "🌐 ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/suportNande")
                ],
                [
                    InlineKeyboardButton(
                        "🍄 ᴍᴀɪɴᴛᴀɪɴᴇʀ", url="https://t.me/Klyuserbot"),
                    InlineKeyboardButton(
                        "🍀 ᴏᴛʜᴇʀ ɪɴғᴏ", callback_data="repoinfo")
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home")
                ]
           ]
        ),
    )



@Client.on_callback_query(filters.regex("cls"))
async def reinfo(_, query: CallbackQuery):
    try:
        await query.message.delete()
        await query.message.reply_to_message.delete()
    except Exception:
        pass


@Client.on_callback_query(filters.regex("repoinfo"))
async def repoinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Selengkapnya Tentang Saya : 
Tidak banyak fitur lainnya dan tolong bergabung dengan saluran atau saluran Instagram.
Repo ini hanya dibuat untuk menyebarkan bot musik yang kuat di heroku tanpa menghadapi masalah pemblokiran akun heroku.
.

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔗 ɢɪᴛʜᴜʙ", url=f"https://github.com/sip-Userbot/Dim-Musik"),
                    InlineKeyboardButton(
                        "💌 Instagram", url=f"https://instagram.com/kanjeng_47?igshid=YmMyMTA2M2Y=")
                ],
                [
                    InlineKeyboardButton(
                        "👾 ʙᴏᴛ ʟɪsᴛs", url="https://t.me/suportsipuserbot"),
                    InlineKeyboardButton(
                        "🤤 ᴘᴏʀɴ ʜᴜʙ", url="http://t.me/suportNande")
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="moreinfo")
                ]
           ]
        ),
     )
    
        
