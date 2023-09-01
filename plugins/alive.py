import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append(f'{amount} {unit}{"" if amount == 1 else "s"}')
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/fa34c7c1016aae47a6354.jpg",
        caption="""**━━━━━━━━━━━━━━━━━
hello, saya bot vc player generasi berikutnya yang super cepat 
dan tidak ada masalah lag dengan kualitas suara terbaik untuk grup telegram
jika ada pertanyaan dm ke pemilik saya [𝐊𝐋𝐘 ༱ 𝐇𝐀𝐍𝐃𝐁𝐄𝐀 🇦🇱](https://t.me/Klyuserbot)...
━━━━━━━━━━━━━━━━━━━**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 sᴜᴘᴘᴏʀᴛ", url="https://t.me/suportsipuserbot"
                    ),
                    InlineKeyboardButton(
                        "📣 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/suportNande"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🧰 ᴄᴏᴍᴍᴀɴᴅs",
                        url="https://telegra.ph/file/fa34c7c1016aae47a6354.jpg",
                    ),
                    InlineKeyboardButton(
                        "⚕️ ᴍᴏʀᴇ ɪɴғᴏ", callback_data="moreinfo"
                    ),
                ],
            ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "/repo"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/fa34c7c1016aae47a6354.jpg",
        caption="""klik pada tombol yang diberikan di bawah ini untuk mengetahui lebih banyak tentang saya. """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="👥 ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/suportsipuserbot"
                    ),
                    InlineKeyboardButton(
                        text="📣 ᴄʜᴀɴɴᴇʟ", url="https://t.me/suportNande"
                    ),
                ]
            ]
        ),
    ) 

@Client.on_message(command(["ping"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢ..... 👀")
    delta_ping = time() - start
    await message.reply_photo(
        photo="https://te.legra.ph/file/2256701b54c183ab45e11.jpg",
        caption=f"ᴘ ᴏ ɴ ɢ ! \n" f"`{delta_ping * 1000:.3f} ᴍs`",
    )

