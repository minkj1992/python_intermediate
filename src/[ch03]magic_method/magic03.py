# Data Model Abstraction
from math import sqrt

distance = lambda x, y: sqrt(sum(((a - b) ** 2 for a, b in zip(x, y))))

# tuple
pt1 = (0, 0)
pt2 = (5, 5)
print(distance(pt1, pt2))
print(pt2)

# namedtuple : class type으로 표현된다.
from collections import namedtuple

Point = namedtuple('Point', 'x y')  # <class '__main__.Point'>
pt3 = Point(0, 0)
pt4 = Point(5, 5)

print(distance(pt3, pt4))
print(pt4)

# NamedTuple : 요소 접근
print(pt4[0], pt4[1])  # 1. index
print(pt4.x, pt4.y)  # 2. name

# NamedTuple 선언 방법
Point0 = namedtuple('Point', 'x y')
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x,y')
Point3 = namedtuple('Point', 'x y')

Point4 = namedtuple('Point', 'x y x class', rename=True)  # 중복, 예약어 이면 _숫자를 key값으로 알아서 변환
pt4 = Point4(1, 2, 7, 8)  # Point(x=1, y=2, _2=7, _3=8)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}
p5 = Point0(**temp_dict)  # unpack
print(p5)  # Point(x=75, y=55)

# Named tuple 메소드

# 1) _make() : list -> 네임드 튜플 ( 단, 인자 갯수가 같아야한다 )
temp = [52, 38]
p4 = Point1._make(temp)
print(p4)

# 2) _fields() : 필드 네임 확인
print(p4._fields)
print(p5._fields)

# 3) _asdict() : OrderedDict 반환
print(p4._asdict())

# 네임드 튜플 Exercise : 20명 per 교실, 4개의 교실(A,B,C,D)

ClassRoom = namedtuple('ClassRoom', ['rank', 'number'])

numbers = map(str, range(1, 21))
ranks = "A B C D".split()

# List Comprehension
students = [ClassRoom(rank, number) for number in numbers for rank in ranks]
print(students)
print(len(students))

# 추천방법
students2 = [ClassRoom(rank, number)
             for rank in "A B C D".split()
             for number in map(str, range(1, 21))]

print(students2)
print(len(students2))

