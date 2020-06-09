"""
Title: 시퀀스(4)
Index:
    1) Immutable Dict & Set
    2) Set Comprehension
    3) Set 선언 최적화
"""

"""1) Dict & Set 심화"""
# Immutable Dict
from types import MappingProxyType

d = {'key' + str(i): 'value' + str(i) for i in range(10)}
# Read Only
d_frozen = MappingProxyType(d)  # Read only

print(d, d_frozen)
d['key2'] = 'value999'
print(d, d_frozen)

# Immutable Set
s1 = {'apple', 'orange', 'apple', 'orange', 'kiwi'}
s2 = set(['apple', 'orange', 'apple', 'orange', 'kiwi'])
s3 = {3}
s4 = {}  # dict
s4 = set()  # set
s5 = frozenset({'apple', 'orange', 'apple', 'orange', 'kiwi'})

"""2) Set Comprehension"""
print('------------------------------')
chr_set = {chr(i) for i in range(256)}
print(chr_set)



"""3) 선언 최적화: {} vs set()"""
# 파이썬은 런타임에 바이트 코드로 인터프리터가 변환 후 실행을 하는데, dis 모드를 사용하면 바이트 코드 순서를 확인 가능
# 결론적으로 { }가 최적화에 좋다.
from dis import dis

print('------------------------------')
print(dis('{10}'))  # 3단계
print('------------------------------')
print(dis('set([10])'))  # 5단계
