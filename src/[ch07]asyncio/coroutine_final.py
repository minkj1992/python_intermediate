# Coroutine -> 단일 스레드, async하게 동작 (제어권, race condition 처리)
# Combining Coroutines with Threads and Process -> non blocking 제공해주기 위해서

import asyncio
import timeit
import threading
from bs4 import BeautifulSoup
from urllib.request import urlopen  # block
from concurrent.futures import ThreadPoolExecutor

# 인코딩
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
# 실행 시작 시간
start = timeit.default_timer()

urls = ['http://daum.net',
        'https://naver.com',
        'http://mlbpark.donga.com/',
        'https://tistory.com',
        'https://wemakeprice.com/']


async def fetch(url, executor):
    # 쓰레드명 출력
    print('Thread Name :', threading.current_thread().getName(), 'Start', url)
    # 실행
    respond = await loop.run_in_executor(executor, urlopen, url)
    soup = BeautifulSoup(respond.read(), 'html.parser')

    result_data = soup.title

    print('Thread Name :', threading.current_thread().getName(), 'Done', url)

    return result_data


async def main():
    executor = ThreadPoolExecutor(max_workers=min(10, len(urls)))

    # future 객체 모아서 gather에서 실행
    futures = [asyncio.ensure_future(fetch(url, executor)) for url in urls]

    result = await asyncio.gather(*futures)

    print()
    print('Result : ', result)


if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()

    loop.run_until_complete(main())

    # 수행 시간 계산
    duration = timeit.default_timer() - start
    print("Total Running Time : ", duration)
