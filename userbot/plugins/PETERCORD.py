import time

from userbot import ALIVE_NAME, StartTime, PETERCORDversion
from PETERCORDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "PETERCORD User"
PETERCORD_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "ππππππππ£πͺ_πΈπ½_ππππππΉπ π₯"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="petercord$"))
@bot.on(sudo_cmd(pattern="petercord$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if PETERCORD_IMG:
        PETERCORD_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        PETERCORD_caption += f"ββββββββββββββββββββββββββββ\n"
        PETERCORD_caption += f"__**ππ’π§ π¦π§ππ§π¨π¦**__\n\n"
        PETERCORD_caption += f"**β π§ππππ§ππ’π‘ π©ππ₯π¦ππ’π‘ :** `1.15.0`\n"
        PETERCORD_caption += f"**β π₯ππππππ’π§ :**`{PETERCORDversion}`\n"
        PETERCORD_caption += f"**β π¨π£π§ππ π :** `{uptime}\n`"
        PETERCORD_caption += f"**β π ππ¦π§ππ₯ :** {mention}\n"
        await alive.client.send_file(
            alive.chat_id, PETERCORD_IMG, caption=PETERCORD_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"ββββββββββββββββββββββββββββ \n"
            f"__**ππ’π§ π¦π§ππ§π¨π¦**__\n\n"
            f"**β π§ππππ§ππ’π‘ π©ππ₯π¦ππ’π‘ :** `1.15.0`\n"
            f"**β π£ππ§ππ₯ππ’π₯πππ’π§ :** `{PETERCORDversion}`\n"
            f"**β π¨π£π§ππ π :** `{uptime}\n`"
            f"**β π ππ¦π§ππ₯ :** {mention}\n",
        )
