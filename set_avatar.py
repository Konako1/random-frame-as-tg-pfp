from pyrogram import Client
from config import id, hash
from bad_apple import get_bad_apple_frame
from datetime import datetime, timedelta

import asyncio

api_id = id
api_hash = hash


async def main():
    while True:
        async with Client('my_account', api_id, api_hash) as app:
            get_bad_apple_frame()

            app: Client
            await app.set_profile_photo(photo='image\\pic.jpg')

            time_now = datetime.now()
            time_to_round = datetime.now() + timedelta(hours=1)

            time_to_sleep = time_to_round - timedelta(
                minutes=time_to_round.minute,
                seconds=time_to_round.second,
                microseconds=time_to_round.microsecond
            )

            sleep_time = time_to_sleep - time_now
            sleep_time = sleep_time.total_seconds()

            print(f"{sleep_time} seconds to reset\n")
            await asyncio.sleep(sleep_time)

if __name__ == '__main__':
    asyncio.run(main())
