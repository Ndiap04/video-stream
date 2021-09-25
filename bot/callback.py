# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import Veez

@Client.on_callback_query(filters.regex("cbenglish"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **HOW TO USE THIS BOT**:
1.)First, add me to your group. 
2.) Then promote me as admin and grant all permission except anonymous admin. 
3.) Add @{Veez.ASSISTANT_NAME} to your group. 
4.) Turn on voice chat first before starting video streaming. 
5.) Type /splay (Reply to video) / (Using youtube link) to start streaming. 
6.) Type /vstop to end the video stream. 

× **Note** × 

- Stream & Stop Command can only be executed by group admin only! 
- The duration is only up to 120 minutes, the more duration you play, the more broken the sound and video will be. 
- Use a short duration so that the sound does not break and is pleasant to hear. 
- Bots cannot make video requests, wait for the video to finish and lower the assistant then play again using the youtube link or reply to the video.

🚨 Maintained by @SpinningEart 🚨""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🇮🇩 Indonesia", callback_data="cbindo")
            ]]
        ))

@Client.on_callback_query(filters.regex("cbindo"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **CARA MENGGUNAKAN BOT INI**:
1.) Pertama, tambahkan saya ke grup Anda.
2.) Kemudian promosikan saya sebagai admin dan berikan semua izin kecuali admin anonim.
3.) Tambahkan @{Veez.ASSISTANT_NAME} ke grup Anda.
4.) Nyalakan obrolan suara terlebih dahulu sebelum mulai streaming video.
5.) Jenis / splay (Balas ke video) / (Memakai link youtube)  untuk mulai streaming.
6.) Jenis / vstop untuk mengakhiri streaming video.

× Catatan ×

- Stream & Stop Command hanya dapat dieksekusi oleh admin grup saja!
- Durasi hanya sampai 120 menit saja, semakin banyak durasi yang kalian play akan semakin patah patah suara dan video nya. 
- Gunakan durasi pendek agar suara tidak patah patah dan enak untuk di dengar.
- Bot tidak bisa melakukan permintaan video, tunggu video selesai dan turunkan assistant lalu play lagi menggunakan link youtube atau balas video.

🚨 Maintained by @SpinningEart 🚨""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "❌ Close", callback_data="cbls")
            ]]
        ))

@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""📚 All Command List:

» /splay (reply to video or yt/live url) - to stream video
» /vstop - stop the video streaming.
» /joinuserbot - invite assistant join to your group.
» /leaveuserbot - order assistant leave from your group.

🔰 EXTRA CMD:

» /tts (reply to text) - text to speak.
» /ping - check bot ping status.
» /uptime - check bot uptime status.

💡 SUDO ONLY:

» /rmd - remove all downloaded files.
» /rmw - remove all downloaded raw files.
» /userbotleaveall - order assistant leave from all group.
» /sysinfo - check bot system information.

🚨 Maintained by @SpinningEart 🚨""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "❌ Close", callback_data="cls")
            ]]
        ))

@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
