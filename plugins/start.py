from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



@Client.on_message(filters.command("start"))
async def start(bot, message):
  m=await message.reply_text("◈◇◇")
  n=await m.edit("◈◈◇")
  p=await n.edit("◈◈◈")
  await p.edit(
    text=f"Hey {message.from_user.mention} ✨,\n\nI am an **advanced** music bot made for **Kerala Music Hub**",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("🍂 Group", url="https://t.me/KeralaMusicHubRedirect"),
        InlineKeyboardButton("🗑️ Close", callback_data="close")
      ]]
    )
  )
  
@Client.on_callback_query(filters.regex("close"))
async def close(bot, query):
  await query.message.delete()
