"""
멀티 프로세싱. 실제 프로세스를 더 생성해서 작업을 처리한다. 
workers를 지정하지 않으면 cpu core만큼의 프로레스를 생성한다
"""
from concurrent import futures

from threds import download_one
from sequential import main

def download_many(cc_list):
    with futures.ProcessPoolExecutor() as executor:
        res = executor.map(download_one, sorted(cc_list))
    print("\n", list(res), end="")
    return len(list(res))

if __name__ == "__main__":
    main(download_many)