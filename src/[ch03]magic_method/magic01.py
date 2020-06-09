# Python Data Model = Special Method(Magic Method)
# -> 클래스 안에 정의할 수 있는 Built-in 메소드
# 파이썬의 핵심 : 1) 시퀀스(Sequence) 2) 반복(Iterator) 3) 함수(Function) 4) 클래스(Class)

# 기본형
print(int, float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10

# inner
print(n + 100)
print(n.__add__(100))
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))


# 클래스 예제 1: 과일 장바구니
# 과일 class + 과일 class

class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return "Fruit Class Info : {}, {} ".format(self._name, self._price)

    def __add__(self, other):
        return self._price + other.price

    def __sub__(self, x):
        return self._price - x.price

    def __le__(self, other):
        return self._price <= other.price

    def __ge__(self, other):
        return self._price >= other.price

    @property
    def price(self):
        print("getter called : ", end='')
        return self._price

    @price.setter
    def price(self, p):
        # print("setter called")
        self._price = p


# 인스턴스 생성
s1 = Fruit("Orange", 7500)
s2 = Fruit("Banana", 3000)

# __add__()
print(s1 + s2)

# __sub__()
print(s1 - s2)
print(s2 - s1)

# __le__(), __ge__()
print(s1 >= s2)
print(s1 <= s2)

# __str__()
print(s1)
print(s2)

# getter
print(s1.price)
print(s1._price) # __변수라면 문제이지만, 싱글 언더라인은 경고만 해준다.
print(s2.price)