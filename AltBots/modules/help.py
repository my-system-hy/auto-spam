from telethon import events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"SEEDHE MAUT ★\n\n» **ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ꜰᴏʀ ʜᴇʟᴘ**\n» **ᴅᴇᴠᴇʟᴏᴘᴇʀ 🥀: @seedhe_maut_owner**"

HELP_BUTTON = [
    [
      Button.inline(" 𝐒ᴘᴀᴍ", data="spam"),
      Button.inline(" 𝐑ᴀɪᴅ ", data="raid")
    ],
    [
      Button.inline(" 𝐄xᴛʀᴀ ", data="extra"),
      Button.url("𝐎𝚆𝙽𝙴𝚁 ", "https://t.me/seedhe_maut_owner")
    ],
    [
      Button.url(" 𝐂ʜᴀɴɴᴇʟ ", "https://t.me/seedhe_maut_owner"),
      Button.url("𝐒ᴜᴘᴘᴏʀᴛ ", "https://t.me/seedhe_maut_owner")
    ],
    [ 
      Button.inline(" SEEDHE MAUT ", data="seedhe_maut_owner")
    ]
  ]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://telegra.ph/file/0381fedca229a87d1ebb4.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(e)}")


extra_msg = f"""
**» ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗨𝘀𝗲𝗿𝗕𝗼𝘁: **SEEDHE MAUT COM**
  1) {hl}ping 
  2) {hl}stop
  3) {hl}sudo <reply to user>  --> Owner Cmd
  4) {hl}logs --> Owner Cmd
  5) gali -- One word gali spam

𝗘𝗰𝗵𝗼: **ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ**
  1) {hl}echo <reply to user>
  2) {hl}rmecho <reply to user>

𝗟𝗲𝗮𝘃𝗲: **ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ**
  1) {hl}leave <group/chat id>
  2) {hl}leave : Type in the Group bot will auto leave that group


**𝗗𝗘𝗔𝗗 𝗫 𝗦𝗣𝗔𝗠  **
"""


seedhe_maut_owner_msg = f"""
**» ɴᴇᴡ ᴄᴏᴍᴍᴀɴᴅs:**

𝗚𝗼𝗼𝗱 𝗔𝗳𝘁𝗲𝗿𝗻𝗼𝗼𝗻: **ᴀғᴛᴇʀ ɴᴏᴏɴ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀ ғᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ**
  1) {hl}ga <count> <username>
  2) {hl}ha <count> <reply to user>

𝗘𝗺𝗼𝗷𝗶: **ᴇᴍᴏᴊɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}saif <count> <username>
  2) {hl}saif <count> <reply to user>

𝗚𝗼𝗼𝗱 𝗠𝗼𝗿𝗻𝗶𝗻𝗴: **ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}gm <count> <username>
  2) {hl}gm <count> <reply to user>

𝗚𝗼𝗼𝗱 𝗡𝗶𝗴𝗵𝘁: **ɢᴏᴏᴅ ɴɪɢʜᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}gn <count> <username>
  2) {hl}gn <count> <reply to user>

𝗙𝗹𝗶𝗿𝘁𝗶𝗻𝗴: **ғʟɪʀᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}flirt <count> <username>
  2) {hl}flirt <count> <reply to user>

𝗕𝗶𝗿𝘁𝗵𝗱𝗮𝘆: **ʙᴅᴀʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ᴡɪsʜ <count> <username>
  2) {hl}ᴡɪsʜ <count> <reply to user>

𝗢𝗻𝗲𝘄𝗼𝗿𝗱𝗚𝗮𝗹𝗶: **ᴏɴᴇ ᴡᴏʀᴅ ɢᴀʟɪ ᴛᴏ ɢᴀɴᴅᴜ ᴜsᴇʀ**
  1) {hl}gali <count> <reply to user>

**𝗗𝗘𝗔𝗗 𝗫 𝗦𝗣𝗔𝗠**
"""
                 
raid_msg = f"""
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗥𝗮𝗶𝗱: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.**
  1) {hl}raid <count> <username>
  2) {hl}raid <count> <reply to user>

𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}rraid <replying to user>
  2) {hl}rraid <username>

𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}drraid <replying to user>
  2) {hl}drraid <username>

𝐌𝐑𝐚𝐢𝐝: **ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}mraid <count> <username>
  2) {hl}mraid <count> <reply to user>

𝐒𝐑𝐚𝐢𝐝: **ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}sraid <count> <username>
  2) {hl}sraid <count> <reply to user>

𝐂𝐑𝐚𝐢𝐝: **ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}craid <count> <username>
  2) {hl}craid <count> <reply to user>


**SEEDHE MAUT SPAM**
"""

spam_msg = f"""
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗦𝗽𝗮𝗺: **ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ.**
  1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
  2) {hl}spam <count> <replying any message>

𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺: **ᴘᴏʀᴍᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ.**
  1) {hl}pspam <count>

𝗛𝗮𝗻𝗴: **ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ.**
  1) {hl}hang <counter>


**𝗗𝗘𝗔𝗗 𝗫 𝗦𝗣𝗔𝗠**
"""                     
           
           
@X1.on(events.CallbackQuery(pattern=r"help_back"))
@X2.on(events.CallbackQuery(pattern=r"help_back"))
@X3.on(events.CallbackQuery(pattern=r"help_back"))
@X4.on(events.CallbackQuery(pattern=r"help_back"))
@X5.on(events.CallbackQuery(pattern=r"help_back"))
@X6.on(events.CallbackQuery(pattern=r"help_back"))
@X7.on(events.CallbackQuery(pattern=r"help_back"))
@X8.on(events.CallbackQuery(pattern=r"help_back"))
@X9.on(events.CallbackQuery(pattern=r"help_back"))
@X10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline(" 𝐒ᴘᴀᴍ ", data="spam"),
                Button.inline(" 𝐑ᴀɪᴅ ", data="raid")
              ],
              [
                Button.inline(" 𝐄xᴛʀᴀ ", data="extra"),
                Button.url(" 𝐎𝚆𝙽𝙴𝚁 ", "https://t.me/seedhe_maut_owner")
              ],
              [          
                Button.url("𝐂ʜᴀɴɴᴇʟ ", "https://t.me/BOTSUPPORT_CHAT"),
                Button.url("𝐒ᴜᴘᴘᴏʀᴛ ", "https://t.me/SAIFALLBOT")
            ],
            [
                Button.inline(" 𝐃ᴇᴀᴅ 𝐗 𝐒ᴘᴀᴍ", data="seedhe_maut_owner")
            ],
           ]
          )
    else:
        await event.answer("ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ  SEEDHE MAUT sᴘᴀᴍ  ʙᴏᴛs !! @seedhe_maut_owner", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"spam"))
@X2.on(events.CallbackQuery(pattern=r"spam"))
@X3.on(events.CallbackQuery(pattern=r"spam"))
@X4.on(events.CallbackQuery(pattern=r"spam"))
@X5.on(events.CallbackQuery(pattern=r"spam"))
@X6.on(events.CallbackQuery(pattern=r"spam"))
@X7.on(events.CallbackQuery(pattern=r"spam"))
@X8.on(events.CallbackQuery(pattern=r"spam"))
@X9.on(events.CallbackQuery(pattern=r"spam"))
@X10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
            buttons=[[Button.inline("< 𝐁ᴀᴄᴋ", data="help_back"),],],
       ) 
    else:
        await event.answer("ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ  SEEDHE MAUT sᴘᴀᴍ  ʙᴏᴛs !! @seedhe_maut_owner", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"raid"))
@X2.on(events.CallbackQuery(pattern=r"raid"))
@X3.on(events.CallbackQuery(pattern=r"raid"))
@X4.on(events.CallbackQuery(pattern=r"raid"))
@X5.on(events.CallbackQuery(pattern=r"raid"))
@X6.on(events.CallbackQuery(pattern=r"raid"))
@X7.on(events.CallbackQuery(pattern=r"raid"))
@X8.on(events.CallbackQuery(pattern=r"raid"))
@X9.on(events.CallbackQuery(pattern=r"raid"))
@X10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< 𝐁ᴀᴄᴋ", data="help_back"),],],
          )
    else:
        await event.answer("ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ  SEEDHE MAUT sᴘᴀᴍ  ʙᴏᴛs !! @seedhe_maut_owner", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"extra"))
@X2.on(events.CallbackQuery(pattern=r"extra"))
@X3.on(events.CallbackQuery(pattern=r"extra"))
@X4.on(events.CallbackQuery(pattern=r"extra"))
@X5.on(events.CallbackQuery(pattern=r"extra"))
@X6.on(events.CallbackQuery(pattern=r"extra"))
@X7.on(events.CallbackQuery(pattern=r"extra"))
@X8.on(events.CallbackQuery(pattern=r"extra"))
@X9.on(events.CallbackQuery(pattern=r"extra"))
@X10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< 𝐁ᴀᴄᴋ", data="help_back"),],],
            )
    else:
        await event.answer("ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ SEEDHE MAUT sᴘᴀᴍ  ʙᴏᴛs !! @seedhe_maut_owner", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"seedhe_maut_owner"))
@X2.on(events.CallbackQuery(pattern=r"seedhe_maut_owner"))
@X3.on(events.CallbackQuery(pattern=r"seedhe_maut_owner"))
@X4.on(events.CallbackQuery(pattern=r"seedhe_maut_owner"))
@X5.on(events.CallbackQuery(pattern=r"seedhe_maut_owner"))
@X6.on(events.CallbackQuery(pattern=r"seedhe_maut_owner"))
@X7.on(events.CallbackQuery(pattern=r"seedhe_maut_owner"))
@X8.on(events.CallbackQuery(pattern=r"seedhe_maut_owner"))
@X9.on(events.CallbackQuery(pattern=r"seedhe_maut_owner"))
@X10.on(events.CallbackQuery(pattern=r"seedhe_maut_owner"))
async def help_seedhe_maut_owner(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(seedhe_maut_owner_msg,
            buttons=[[Button.inline("< 𝐁ᴀᴄᴋ", data="help_back"),],],
       ) 
    else:
        await event.answer("ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ SEEDHE MAUT sᴘᴀᴍ  ʙᴏᴛs !! @seedhe_maut_owner", cache_time=0, alert=True)

