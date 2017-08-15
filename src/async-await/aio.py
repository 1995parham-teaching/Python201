# In The Name Of God
# ========================================
# [] File Name : aio.py
#
# [] Creation Date : 09-08-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from aiohttp import web
import asyncio


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    await asyncio.sleep(10)
    text = "Hello, " + name
    return web.Response(text=text)


app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)


web.run_app(app)
