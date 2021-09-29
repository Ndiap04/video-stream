# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import Veez

@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **HOW TO USE THIS BOT**:
1.)First, add me to your group. 
2.) Then promote me as admin and grant all permission except anonymous admin. 
3.) Add @SpinningEarth2_Assistant to your group or you can use /joinuserbot. 
4.) Turn on voice chat first before starting video streaming. 
5.) Type /splay (Reply to video) / (Using youtube link) to start streaming. 
6.) Type /vstop to end the video stream. 

× **Note** × 

- Stream & Stop Command can only be executed by group admin only! 
- The duration is only up to 60 minutes, the more duration you play, the more broken the sound and video will be. 
- Use a short duration so that the sound does not break and is pleasant to hear. 
- Bots cannot make video requests, wait for the video to finish and lower the assistant then play again using the youtube link or reply to the video.

🚨 Maintained by @SpinningEart 🚨""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "❌ Close", callback_data="cls")
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
