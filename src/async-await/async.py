# In The Name Of God
# ========================================
# [] File Name : async.py
#
# [] Creation Date : 15-08-2017
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================
import asyncio


async def hello():
    print("Hello")


loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
