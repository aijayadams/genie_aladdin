#!/usr/env python3

from genie_aladdin import api
import asyncio

async def main():
    a = api.AladdinConnection("myemailaddreess@isp.com", "supersecretpassword")
    await a.connect()
    await a.discover_doors()
    await a.close_door()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
