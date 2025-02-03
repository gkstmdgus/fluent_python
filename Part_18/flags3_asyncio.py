"""
flag2에서는 get_flag()를 코루틴으로 변경해서 병목을 줄였지만 아직 save_flag에 대한 병목을 처리하지는 못했다. 
멀티 스레딩을 사용하는 경우, 기본적으로는 GIL로 병렬처리가 불가하지만 Block I/O에 대해서 GIL을 해제하여 병렬처리가 가능했다.
하지만 asyncio의 경우 단일 스레드를 사용하므로 이벤트 루프의 스레드가 블록처리 된다. 
그렇기 때문에 디스크 입출력에 대한 함수도 수정이 필요하다.

loop.run_in_executer()함수를 사용하여 외부 스레드를 제공하여 디스크 입출력을 하면 문제가 해결된다.
"""
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
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, save_flag, image, cc.lower() + ".gif")
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
    import time
    time.sleep(2)
    loop.close()
    return len(counts)

if __name__ == "__main__":
    main(download_many)