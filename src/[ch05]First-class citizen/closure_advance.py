"""
Title: Closure 심화
Index:
    1) 클로저 사용 예제
    2) 잘못된 클로저 사용
    3) 클로저 정리
"""


# 클로저(Closure) 사용
def closure_ex1():
    # Free variable
    series = []

    # 클로저 영역
    def averager(v):
        # series = [] # 주석 해제 후 확인
        series.append(v)
        print('{}th inner >>> {} / {}'.format(v, series, len(series)))
        return sum(series) / len(series)

    # 함수를 return
    return averager


avg_closure1 = closure_ex1()

print(avg_closure1(15))
print(avg_closure1(35))
print(avg_closure1(40))

print()
print()

# function inspection

print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print()
print(avg_closure1.__code__.co_freevars)
print()
print(dir(avg_closure1.__closure__[0]))
print()
print(avg_closure1.__closure__[0].cell_contents)

print()
print()


# 잘못된 클로저 사용
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1  # cnt = cnt + 1
        total += v
        return total / cnt

    return averager


avg_closure2 = closure_ex2()


# print(avg_closure2(15)) # 예외


# Nonlocal -> Free variable
def closure_ex3():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure3 = closure_ex3()

print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))

print()
print()
