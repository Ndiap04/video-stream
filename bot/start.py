# Copyright (C) 2021 By VeezMusicProject

from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from config import Veez
from helpers.decorators import sudo_users_only
from helpers.filters import command

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
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{Veez.BOT_USERNAME}"]))
async def start(_, m: Message):
    if m.chat.type == "private":
        await m.reply_text(
            f"✨ **Hello there, I am a telegram group video streaming bot.**\n\n💭 **I was created to stream videos in group "
            f"video chats easily.**\n\n❔ **To find out how to use me, please press the help button below** 👇🏻",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕", url=f"https://t.me/{Veez.BOT_USERNAME}?startgroup=true")
                ], [
                    InlineKeyboardButton(
                        "❔ HOW TO USE THIS BOT STREAM-V", callback_data="cbguide")
                ], [
                    InlineKeyboardButton(
                        "📚 Command List Stream Video", callback_data="cblist")
                ], [
                    InlineKeyboardButton(
                        "📚 Command List Music VC", url="https://telegra.ph/%CF%9A%D6%84%C3%AC%D5%B2%D5%B2%C3%AC%D5%B2%D6%81--%C6%90%C4%85%C9%BE%D5%A7%D5%B0-1-09-16")
                ], [
                    InlineKeyboardButton(
                        "🚨 Channel Support", url="https://t.me/SpinningEart")
                ]]
            ))
    else:
        await m.reply_text("**I'am Online!**",
                           reply_markup=InlineKeyboardMarkup(
                               [[
                                   InlineKeyboardButton(
                                       "📚 Command List Stream Video", url="https://t.me/SpinningEarth1_Bot?start=help")
                               ], [
                                   InlineKeyboardButton(
                                       "📚 Command List Music VC", url="https://telegra.ph/%CF%9A%D6%84%C3%AC%D5%B2%D5%B2%C3%AC%D5%B2%D6%81--%C6%90%C4%85%C9%BE%D5%A7%D5%B0-1-09-16")
                               ], [
                                   InlineKeyboardButton(
                                       "🚨 Channel Support", url=f"https://t.me/SpinningEart")
                               ]]
                           )
                           )
