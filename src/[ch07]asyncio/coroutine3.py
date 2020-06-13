import time
import asyncio
from urllib.request import urlopen

urls = ('http://daum.net',
        'https://naver.com',
        'http://mlbpark.donga.com/',
        'https://tistory.com',
        'https://wemakeprice.com/')


async def get_url_data(url: str) -> (str, str, str):
    '''특정 URL에 요청을 보내어 HTML 문서를 문자열로 받는다.
    url, 응답텍스트, 포맷팅된 소요시간을 리턴한다.'''
    print(f'Request for: {url}')
    s = time.time()
    res = urlopen(url)
    data = res.read()
    return url, data, f'{time.time() - s: .3f}'


async def test_urls(func, urls):
    s = time.time()
    fs = {func(url) for url in urls}
    for f in asyncio.as_completed(fs):
        url, body, t = await f
        print(f'Resonse from: {url}, {len(body)}Bytes - {f}sec')
    print(f'{time.time() - s:0.3f}sec')


loop = asyncio.get_event_loop()
loop.run_until_complete(test_urls(get_url_data, urls))
