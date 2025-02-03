import asyncio

import aiohttp

from Part_17.sequential import BASE_URL, save_flag, show, main

async def get_flag(cc):
    cc = cc.lower()
    url = f"{BASE_URL}/{cc}/{cc}.gif"
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as resp:
            image = await resp.read()
    return image

async def download_one(cc):
    image = await get_flag(cc)
    show(cc, 200, "OK")
    save_flag(image, cc.lower() + ".gif")
    return cc

def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in cc_list]
    # asyncio.wait(list)는 입력받은 코루틴, 퓨처 객체의 리스트를 하나의 Task 객체로 매핑한다.
    wait_coro = asyncio.wait(to_do)
    # 실행이 완료된 집합, 실행이 완료되지 않은 집합
    result, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(result)

if __name__ == "__main__":
    main(download_many)