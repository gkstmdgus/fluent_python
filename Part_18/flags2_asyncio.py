import asyncio
import collections

import aiohttp
from aiohttp import web

from Part_17.sequential import BASE_URL, save_flag, show, main

async def get_flag(cc):
    cc = cc.lower()
    url = f"{BASE_URL}/{cc}/{cc}.gif"
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as resp:
            if resp.status == 200:
                image = await resp.read()
                return image
            elif resp.status == 404:
                raise web.HTTPNotFound()
            else:
                raise aiohttp.ServerConnectionError(
                    code=resp.status, message=resp.reason, headers=resp.headers
                )

async def download_one(cc, semaphore):
    try:
        async with semaphore:
            image = await get_flag(cc)
    except web.HTTPNotFound:
        status = 404
        msg = 'not found'
    else:
        save_flag(image, cc.lower() + ".gif")
        status = 200
        msg = "OK"

    show(cc, status, msg)
    return status

async def downloader_coro(cc_list, concur_req):
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(concur_req)
    to_do = [download_one(cc, semaphore) for cc in cc_list]

    to_do_iter = asyncio.as_completed(to_do)
    for future in to_do_iter:
        try:
            res = await future
        except Exception as e:
            status = 404
        else:
            status = 200
        
        counter[status] += 1
    
    return counter

def download_many(cc_list):
    concur_req = 3
    loop = asyncio.get_event_loop()
    coro = downloader_coro(cc_list, concur_req)
    print(coro)
    counts = loop.run_until_complete(coro)
    loop.close()
    return len(counts)

if __name__ == "__main__":
    main(download_many)