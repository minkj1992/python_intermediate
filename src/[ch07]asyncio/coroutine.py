# Coroutine -> 단일 스레드, async하게 동작 (제어권, race condition 처리)
# Combining Coroutines with Threads and Process -> non blocking 제공해주기 위해서

import asyncio
import timeit
from urllib.request import urlopen  # block
from concurrent.futures import ThreadPoolExecutor
import threading

# 실행 시작 시간
start = timeit.default_timer()

urls = ['http://daum.net',
        'https://naver.com',
        'http://mlbpark.donga.com/',
        'https://tistory.com',
        'https://wemakeprice.com/']


def fetch(url, executor):
    pass


async def main():
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체 모아서 gather에서 실행
    futures = [asyncio.ensure_future(fetch(url,executor)) for url in urls]
    

if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()

    loop.run_until_complete(main())

    # 수행 시간 계산
    duration = timeit.default_timer() - start
    print("Total Running Time : ", duration)
