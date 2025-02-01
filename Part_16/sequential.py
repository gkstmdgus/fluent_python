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
    return resp.content

def show(text):
    print(text, end=" ")
    sys.stdout.flush()

def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + ".gif")
    return len(cc_list)

def main(download_many):
    t0 = time.time()
    count = download_many(POP10_CC)
    elapsed = time.time() - t0
    print(f"\n{count} flags downloads in {elapsed:.2f}s")

if __name__ == "__main__":
    """약 18초 정도 소요"""
    main(download_many)
