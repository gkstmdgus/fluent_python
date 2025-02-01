import os
import time
import sys
import requests

POP10_CC = ('CN IN US ID BR PK NG BD RU JP').split()

BASE_URL = "http://flupy.org/data/flags"

DEST_DIR = "downloads/"

def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)

def get_flag(cc):
    cc = cc.lower()
    url = f"{BASE_URL}/{cc}/{cc}.gif"
    resp = requests.get(url)
    if resp.status_code != "200":
        resp.raise_for_status()
    return resp.content

def show(text, status, msg):
    print(f"{status}: {text}. msg: {msg}")

def download_one(cc):
    try:
        image = get_flag(cc)
    except requests.exceptions.HTTPError as exc:
        res = exc.response
        if res.status_code == 404:
            # 404에러 이외의 예외는 download_many()함수로 전달
            status = res.status_code
            msg = "not found"
        else:
            raise exc
    else:
        save_flag(image, cc.lower() + ".gif")
        status = 200
        msg = "OK"
        
    show(cc, status, msg)
    return cc

def download_many(cc_list):
    for cc in sorted(cc_list):
        try:
            download_one(cc)
        except requests.exceptions.HTTPError as exc:
            res = exc.response
            print(f'HTTP error {res.status_code} - {res.reason}')
        except requests.exceptions.ConnectionError as exc:
            print('Connection error')
    return len(cc_list)

def main(download_many):
    t0 = time.time()
    count = download_many(POP10_CC)
    elapsed = time.time() - t0
    print(f"\n{count} flags downloads in {elapsed:.2f}s")

if __name__ == "__main__":
    """약 18초 정도 소요"""
    main(download_many)
