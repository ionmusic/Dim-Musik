# sip-Userbot // @sip-userbot

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from modules.helpers.filters import command, other_filters
from modules.helpers.decorators import sudo_users_only, errors

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command(["rmd", "clear"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    if ls_dir := os.listdir(downloads):
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **menghapus semua file unduhan**")
    else:
        await message.reply_text("❌ **tidak ada file yang diunduh**")

        
@Client.on_message(command(["rmw", "clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    if ls_dir := os.listdir(raw_files):
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("✅ **menghapus semua file unduhan**")
    else:
        await message.reply_text("❌ **tidak ada file yang diunduh**")


@Client.on_message(command(["cleanup"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    if ls_dir := os.listdir(pth):
        for _ in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("✅ **dibersihkan**")
    else:
        await message.reply_text("✅ **sudah siap dibersihkan**")
