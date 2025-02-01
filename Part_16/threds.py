"""
멀티 스레딩. ThreadPoolExecutor.map()을 이용해서 여러개의 스레드(최대 workers)에서 다운로드 진행
실제로 파이썬은 GIL(Global Interpreter Lock)으로 인해서 하나의 파이썬 바이트 코드에 하나의 쓰레드만 접근 가능 
실질적으로 병령 처리는 이루어지지 않고 Sync-Nonblock 방식으로 처리됨. 
하지만 Block I/O에 대해서는 자체적으로 GIL을 해제하므로 해당 예시에서는 성능향상이 있음
실질적으로 계산이 필요한 연산은 멀티 프로세싱을 이용해서 병령 처리 진행. 
"""
from concurrent import futures

from sequential import save_flag, get_flag, show, main

MAX_WORKERS = 5

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + ".gif")
    return cc

def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))
    print("\n", list(res), end="")
    return len(list(res))

def download_many_with_as_complete(cc_list):
    """
    ThreadPoolExecutor.map() 함수는 입력처리된 스레드 순서대로 결과를 출력한다. 
    만약, 처음들어온 스레드의 작업이 10초 걸리고 두번째 스레드의 작업이 2초 걸린다면 두 번째 작업이 먼저 종료될것이다.
    하지만 map() 함수는 순서를 지키므로 첫 번째 작업이 마칠때까지 두 번째 결과는 대기한다. 
    입력 순서와 상관없이 완료되는대로 결과를 받기를 원하면 submit()/as_complete() 조합을 사용한다. 
    이 조합의 다른 장점은 여러가지의 future를 사용할 수 있다.
    """
    with futures.ThreadPoolExecutor(MAX_WORKERS) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            print(f"Scheduled for {cc}: {future}")
        
        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            print(f"{future} result: {res!r}")
            results.append(res)
    return len(results)

if __name__ == "__main__":
    """약 4초 소요. worker수를 늘리면 더 빨라진다."""
    main(download_many)