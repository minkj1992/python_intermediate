import asyncio
import random
import time


# async def: 코루틴 함수(asyncio.coroutine을 생성해주는 함수)
# 코루틴 함수를 호출하면  asyncio.coroutine(객체)를 return 한다.
# await: async def block 안에서 사용되며, awaitable 한 객체가 뒤에 나온다. (Task, Future, Coroutine)
async def lazy_greet(msg, delay=1):
    print(msg, "will be displayed in", delay, "seconds")
    await asyncio.sleep(delay)  # sleep 시간이 끝나기전까지 해당 async block을 떠나있는다. event_loop가 action이 완료되면 알려주어 여기로 제어권이 사용되도록 한다.
    print("back to {}".format(msg))
    return msg.upper()


# ensure_future(): event_loop에 코루틴을 스케줄링
async def main():
    messages = ['hello', 'world', 'apple', 'banana', 'cherry']
    times = sorted([10, 10, 10, 10, 0.001])
    fts = [asyncio.ensure_future(lazy_greet(m, i)) for i, m in zip(times, messages)]  # 등록만 진행, 실행 x

    # as_completed(스케줄링된 코루틴으로부터 결과 받아온다): 이터레이터 리턴, 먼저 끝나는 것부터 차례로 순회하여 반복문을 돌린다. ( 즉 요청을 먼저 보내고, 결과값 먼저 온것부터 loop를 돌린다.)
    for f in asyncio.as_completed(fts):
        print(await f)  # 처음에 모든 task들에게 요청 이후 함수의 await에 의해 다시 권한 받고 먼저 끝나는 task가 하나라도 나타난다면 loop 진행 (return 또는 await 전까지 실행)
        print("back to main()")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())  # until main() end loop is run
loop.close()
