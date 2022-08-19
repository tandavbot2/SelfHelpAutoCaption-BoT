import pyrogram, os, asyncio

try: api_id = int(os.environ.get("api_id", None))
except Exception as api_id: print(f"⚠️ Api ID Invalid {api_id}")
try: api_hash = os.environ.get("api_hash", None)
except Exception as api_id: print(f"⚠️ Api Hash Invalid {api_hash}")
try: bot_token = os.environ.get("bot_token", None)
except Exception as bot_token: print(f"⚠️ Bot Token Invalid {bot_token}")
try: custom_caption = os.environ.get("custom_caption", "`{file_name}`")
except Exception as custom_caption: print(f"⚠️ Custom Caption Invalid {custom_caption}")
try: username = os.environ.get("bot_username", None)
except Exception as username: print(f"⚠️ Add UserName {username}")

AutoCaptionBotV1 = pyrogram.Client(
   name="AutoCaptionBotV1", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

start_message = """
<b>👋Hello {}</b>
<b>I am an AutoCaption bot</b>
<b>All you have to do is add me to your channel and I will show you my power</b>
<b>@Mo_Tech_YT</b>"""

about_message = """
<b>• Name : AutoCaption V1</b>
<b>• Language : Python3</b>
<b>• Updates : <a href=https://t.me/Mo_Tech_YT>Click Here</a></b>
<b>• Source Code : <a href=https://t.me/TeamEvamaria>Click Here</a></b>"""

@AutoCaptionBotV1.on_message(pyrogram.filters.private & pyrogram.filters.command(["start"]))
def start_command(bot, update):
  update.reply(start_message.format(update.from_user.mention), reply_markup=pyrogram.types.InlineKeyboardMarkup(start_button), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBotV1.on_callback_query(pyrogram.filters.regex("start"))
def strat_callback(bot, update):
  update.message.edit(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBotV1.on_callback_query(pyrogram.filters.regex("about"))
def about_callback(bot, update):  
  update.message.edit(about_message, reply_markup=about_buttons(bot, update), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBotV1.on_message(pyrogram.filters.channel)
def edit_caption(bot, update: pyrogram.types.Message):
  motech, _ = get_file_details(update)
  try: update.edit(custom_caption.format(file_name=motech.file_name))
  except pyrogram.errors.FloodWait as FloodWait:
      asyncio.sleep(FloodWait.x)
      update.edit(custom_caption.format(file_name=motech.file_name))
     
def get_file_details(update: pyrogram.types.Message):
  if update.media:
    for message_type in (
        "photo",
        "animation",
        "audio",
        "document",
        "video",
        "video_note",
        "voice",
        # "contact",
        # "dice",
        # "poll",
        # "location",
        # "venue",
        "sticker"
    ):
        obj = getattr(update, message_type)
        if obj:
            return obj, obj.file_id

def start_buttons(bot, update):
  buttons = [[
   pyrogram.types.InlineKeyboardButton("Updates", url="t.me/Mo_Tech_YT"),
   pyrogram.types.InlineKeyboardButton("About 🤠", callback_data="about")
   ],[
   pyrogram.types.InlineKeyboardButton("➕️ Add To Your Channel ➕️", url=f"http://t.me/{username}?startchannel=true")
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

def about_buttons(bot, update):
  buttons = [[
   pyrogram.types.InlineKeyboardButton("🏠 Back To Home 🏠", callback_data="start")
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)
  
AutoCaptionBotV1.run()