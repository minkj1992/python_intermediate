# 강의 질문

안녕하십니까 강사님.

좋은 강의 감사드립니다. 덕분에 많은 것들을 배울 수 있었습니다. 강의를 마무리하며 최종적으로 3가지 질문을 드리고 싶은데요.

마지막 강의에서와 같이 asyncIO에 loop.run_in_executor(executor, urlopen, url)를 사용하게 된다면

1) 제가 이해 한바에 의하면 asyncIO의 event loop는 node.js처럼 main thread와는 별도로 동작하는 thread로 계속 loop를 돈다고 이해하고 있는데 제가 이해한 것이 맞을까요? 

2) 강의에서 asyncIO + threadpoolExecutor 개념은 event loop에서만 GIL에 접근을 하며, 나머지 코루틴들에 대해서는 thread에게 IO wait을 위임하여 event loop가 Blocking 되지 않고, 멀티 쓰레드 상황에서도 GIL block을 먹지 않는 기술일까요?

3) 파이썬을 실행하고 있는 프로세스에서 os에게 IO bound task를 위임해주는 방법은 존재하지 않나요?

제가 생각하기에 일일이 요청들에 대해서 thread로 감싸주는 것이 아니라, 파이썬 레벨에서 event loop를 돌면서 IO 요청들에 대해서 코루틴을 생성한 뒤, kernel thread에게 request를 위임해주고, 커널 쓰레드가 os에 async하게 IO 요청을 보내주고

이후 os 레벨에서 IO interrupt가 일어날때, python event loop는 잠시 루프를 멈추고 데이터를 전달받아, 해당 IO에 매핑된 코루틴에게 데이터를 전달해주면, 코루틴은 중지되었던 위치에서 값을 전달받아 이후 로직을 진행해주면 될 것같다고 생각되는데 불가능한 방법일지 궁금합니다.
