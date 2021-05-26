# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) 
# Made by @diemmmmmmmmmm...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in PETERCORD Userbot by @diemmmmmmmmmm

import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, PETERCORDversion
from PETERCORDBOT.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins

# TENTANG AKU DAN DIA
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝕄𝔸𝔽𝕀𝔸𝔹𝕆𝕋"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @diemmmmmmmmmm (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for @diemmmmmmmmmm

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

PETERCORD = bot.uid

edit_time = 10
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/b52e42266a323cbe9f849.jpg"
file2 = "https://telegra.ph/file/e4142fc1d14bc3c8181a3.jpg"
file3 = "https://telegra.ph/file/b52e42266a323cbe9f849.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "  __**🎖PETERCORD ALIVE🎖**__\n\n"

pm_caption += (
    f"                 🎖PENGGUNA🎖\n**  『🎖[{DEFAULTUSER}](tg://user?id={PETERCORD})🎖』**\n\n"
)

pm_caption += "TELETHON : `1.15.0` \n\n"

pm_caption += f"PETERCORD  : `{PETERCORDversion}`\n\n"

pm_caption += f"SUDO       : `{sudou}`\n\n"

pm_caption += "GRUP SUPPORT: [ᴊᴏɪɴ](https://t.me/TEAMSquadUserbotSupport)\n\n"

pm_caption += "OWNERS  : [ILHAM MANSIEZ](https://t.me/diemmmmmmmmmm)\n\n"

pm_caption += "SUPPORT    :[ⓃⒾⓈⒽⓊ](https://t.me/TEAMSquadUserbotSupport)\n\n"

pm_caption += "      [𝗥𝗘𝗣𝗢](https://github.com/ilham77mansiz/-PETERCORD-) 🔹 [OWNER](https://t.me/diemmmmmmmmmm)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file1)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file2)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file3)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
