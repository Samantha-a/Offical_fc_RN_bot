import asyncio
from bot.client import Client
from bot.core.db.add import (
    add_user_to_database
)
from pyrogram import (
    filters,
    types
)


@Client.on_message((filters.video | filters.audio | filters.document) & ~filters.edited)
async def on_media_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await bot.send_message(
        chat_id=update.chat.id,
        text="**Should I show File Information?**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('📝Rename', callback_data = "rnme"),
                    InlineKeyboardButton('📂File To Video', callback_data = "f2v")
                ],
                [
                    InlineKeyboardButton('🎞️Custom Thumbnail', callback_data = "cthumb"),
                    InlineKeyboardButton('📑Custom Caption', callback_data = "ccaption")
                ],
                [
                    InlineKeyboardButton('💬About', callback_data = "about")
                ]
            ]
        )
    )
        disable_web_page_preview=True,
        reply_to_message_id=m.message_id
    )
