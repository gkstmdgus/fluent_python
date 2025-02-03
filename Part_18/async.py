"""
asyncio
단일 스레드. 이벤트 루프와 코루틴을 기반으로 한 비동기 프레임워크. 코루틴으로 동시성 제공 

Future
작업의 상태와 실행 결과를 저장하는 객체 (awaitable)
실행은 할 수 없다. 

Task
Future를 상속받으며 실행까지 담당한다. 입력으로 코루틴을 받으며 `__coro`에 저장한다.
`asyncio.run(coro)`나 `asyncio.create_task(coro)`를 실행하면 Task 객체를 생성한다.

흐름 
1. asyncio.run(coro) 함수로 이벤트 루프 생성 
2. 입력받은 코루틴(coro)을 Task로 변환 후 실행 (send() 실행)
3. 작업을 진행하다가 await I/O와 직면 (Future 객체를 await하도록 설계되어 있음)
    3-a. 소켓이 등록되어 있는 경우 
        1. `yield `로 제어권 반환 
    3-b. 소켓이 등록되어 있지 않은 경우 
        1. socket 등록 후 future객체 생성해서 await 
        2. `yield Future`
4. Task 객체의 처리 
    4-a. `yield `로 반환된 경우
        1. 자신의 실행을 이벤트 루프에 실행 예약 
    4-b. `yield Future`로 반환된 경우 
        1. Future 객체를 Task에 저장 
        2. Future.add_done_callback()에 완료 후 이벤트 루프에 등록할 함수 저장
5. 다시 이벤트 루프로 돌아와서 쌓여있는 작업 처리
6. 작업이 없는 경우 select()함수로 소켓의 상태 확인 
    6-a. 완료된 소켓이 있으면 결과를 Future.result에 등록 (상태 변화)
    6-b. future의 add_done_callback()에 등록된 함수 이벤트 루프에 등록 
8. 이벤트 루프의 작업을 처리하다가 Task 차례
    8-a. 작업이 완료된 future는 Task에서 바인딩 해제 
    8-b. 더이상 대기중인 future가 없으므로 해당 await는 끝내고 다음으로 send()
9. 이렇게 입력 코루틴이 return될때까지 반복
10. 이벤트 루프 종료

[참고]: https://velog.io/@heyoni/python-asyncio-3
"""
import asyncio

async def sleep(sec=3):
    print(f"Start Sleep: {sec}")
    await asyncio.sleep(sec)
    print(f"Done sleep: {sec}")
    return sec

async def main():
    coros = [asyncio.create_task(sleep(i)) for i in range(1,5)]
    await asyncio.sleep(2)
    print("Done Sleep main")
    results = await asyncio.gather(*coros)
    print(results)

if __name__ == "__main__":
    asyncio.run(main())