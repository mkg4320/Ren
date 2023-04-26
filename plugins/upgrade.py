from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0 Free 🐍
	
	**VIP 1 ** 
	Daily  Upload  limit 10GB
	Price Rs 100  🇮🇳/🌎 1.5$  Unlocks 🔓 Lifetime 
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 200  🇮🇳/🌎 4$  Unlocks 🔓 Lifetime 
	
	Pay Using Upi I'd ```Conatact Dev @Aay700```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Aay700")], 
        			[InlineKeyboardButton("Movies World🌎",url = "https://t.me/blackest_harbour"),
        			InlineKeyboardButton("Series 🍿 ",url = "https://t.me/z_harbour_files")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0 Free 
	
	**VIP 1 ** 
	Daily  Upload  limit 10GB
	Price Rs 100  🇮🇳/🌎 Unlocks 🔓 Lifetime
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 200  🇮🇳/🌎 No Service Validity 😜
	
	
	Pay Using Upi I'd ```Contact Dev @sigma_male_007```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Aay700")], 
        			[InlineKeyboardButton("Movies 🌎",url = "https://t.me/blackest_harbour"),
        			InlineKeyboardButton("Series",url = "https://t.me/z_harbour_files")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
