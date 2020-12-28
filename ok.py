from telethon import events
import asyncio
import os
import sys
i = 1000

@borg.on(events.NewMessage(pattern=r"\.ok", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       

    await event.edit("1000")
    await asyncio.sleep(1)
    await event.edit(i-7)
    await asyncio.sleep(1)
    await event.edit(i-7)
    await asyncio.sleep(1)
    await event.edit(i-7)
    await asyncio.sleep(1)
    await event.edit(i-7)
    await asyncio.sleep(1)
    await event.edit(i-7)
    await asyncio.sleep(1)
    await event.edit(i-7)
    await asyncio.sleep(1)
    await event.edit(i-7)
    await asyncio.sleep(1)
    await event.edit(i-7)
    await asyncio.sleep(1)
    await event.edit("БОМБИТ С ТЕБЯ!")
