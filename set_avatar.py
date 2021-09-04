from pyrogram import Client, idle
from pyrogram.raw import functions
from pyrogram.types import Message

from config import id, hash, test_group_id
from bad_apple import get_bad_apple_frame
from datetime import datetime, timedelta
from asyncio import create_task

import asyncio

api_id = id
api_hash = hash
app = Client('my_account', api_id, api_hash)


@app.on_message()
async def pfp_changer(_, message: Message):
    if message.chat.id != test_group_id:
        return
    if message.text == 'NeNicePfp_FUCKING_ALERT1337':
        await app.read_history(test_group_id)
        await update_pfp()


async def endless_updater():
    while True:
        await update_pfp()

        time_now = datetime.now()
        time_to_round = datetime.now() + timedelta(hours=1)

        time_to_sleep = time_to_round - timedelta(
            minutes=time_to_round.minute,
            seconds=time_to_round.second,
            microseconds=time_to_round.microsecond
        )

        sleep_time = time_to_sleep - time_now
        sleep_time = sleep_time.total_seconds()

        print(f"\n{sleep_time} seconds to reset\n")
        await asyncio.sleep(sleep_time)


async def update_pfp():
    frame = get_bad_apple_frame()
    await app.set_profile_photo(photo='image\\pic.jpg')
    await app.send(
        functions.account.UpdateProfile(
            about=f'Current frame: {frame}'
        )
    )
    photos = await app.get_profile_photos("me", limit=2)
    await app.delete_profile_photos(photos[1].file_id)


async def main():
    async with app:
        create_task(endless_updater())
        await idle()

if __name__ == '__main__':
    app.run(main())
