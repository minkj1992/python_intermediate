"""
Title: 시퀀스(3)
Index:
    1) 해시 테이블
    2) Dict 생성 고급 예제
    3) Setdefault 사용법
"""

# 1) 해시 테이블: Python 엔진은 기본적으로 Hash로 구성

# Dict 구조
# print(__builtins__.__dict__)

# Hash 값 확인 (고유해야 한다 = Immutable)
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])
for t in t1, t2:
    try:
        print(hash(t))
    except Exception as e:
        print("예외 발생 : ", e)

# Dict Setdefault: Tuple에서 dict 만들때 레퍼런스 권장 사항(recommend)
# -> 대용량 데이터 처리에 효과적, 빠른 속도
# 예시: 키가 중복되어있는 2중 튜플
source = (('k1', 'v1'),
          ('k1', 'v2'),
          ('k2', 'v3'),
          ('k2', 'v4'),
          ('k2', 'v5'))

new_dict1 = {}
new_dict2 = {}

# Not use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v, ]
print(new_dict1)

# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)  # wow .... 대박, defaultdict과 차이점은? defaultdict이 더 빠르다.
print(new_dict2)
