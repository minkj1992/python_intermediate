"""
Title: 시퀀스(2)
Index:
    1) Tuple 고급 사용
    2) Mutable vs Immutable
    3) Sort vs Sorted
"""

# 1) Tuple Advanced
# Unpacking
x, y, *rest = range(10)
print(x, y, rest)  # 0 1 [2, 3, 4, 5, 6, 7, 8, 9]

x, y, *rest = range(2)
print(x, y, rest)  # 0 1 []

# 2) Mutable vs Immutable

l = (15, 20, 30)
m = [15, 20, 30]
print(*map(id, (l, m)))  # 139622101366104 139622101469576

l = l * 2  # (15, 20, 30, 15, 20, 30)
m = m * 2  # [15, 20, 30, 15, 20, 30]
print(*map(id, (l, m)))  # 139622101751656 139622101471112

l *= 2  # (15, 20, 30, 15, 20, 30, 15, 20, 30, 15, 20, 30)
m *= 2  # [15, 20, 30, 15, 20, 30, 15, 20, 30, 15, 20, 30]
print(*map(id, (l, m)))  # 139622101863736 139622101471112

# 3) Sort(원본) vs Sorted (새로운 객체)
# -> reverse, ley = len, key = str.lower, key = lambda x: ...
fruit_list = ['orange', 'apple', 'coconut', 'banana', 'lemon', 'lime']

# sorted
print(sorted(fruit_list, reverse=True))
print(sorted(fruit_list, key=len))
print(sorted(fruit_list, key=lambda x: x[-1]))
print(sorted(fruit_list, key=lambda x: x[-1], reverse=True))

# sort
fruit_list.sort()
fruit_list.sort(reverse=True)
fruit_list.sort(key=len)
fruit_list.sort(key=lambda x: x[-1])
fruit_list.sort(key=lambda x: x[-1],reverse=True)

# List vs Array
# list: 융통성, 다양한 자료형, 범용적 사
# Array : 숫자용 기반, 리스트와 거의 호환
