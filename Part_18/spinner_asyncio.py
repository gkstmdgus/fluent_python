"""
asyncio 사용하는 버전. 
- asyncio.Task와 threading.Tread와 대등하다고 생각하면 된다. 
- Task는 코루틴을 구동하고 Thead는 콜러블을 호출한다. 
- await == yield from
"""
import itertools
import asyncio
import sys

async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            await asyncio.sleep(1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))

async def slow_function(wait_time=3):
    await asyncio.sleep(wait_time)
    return 42

async def supervisor():
    spinner = asyncio.create_task(spin('thinking!'))
    print('spinner oject: ', spinner)
    result = await slow_function()
    spinner.cancel()
    return result

def main():
    result = asyncio.run(supervisor())
    print('Answer: ', result)

if __name__ == "__main__":
    main()