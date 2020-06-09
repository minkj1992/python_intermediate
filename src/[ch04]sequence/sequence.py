# 시퀀스형(2)
# 1) 컨테이너([list, tuple, collections.deque])
# 2) 플랫(Flat, 한개의 자료형, [str, bytes, bytearray, array.array, memoryview])
# Immutable: tuple, str, bytes

# 4-1. Comprehending Lists
chars = "+_)(*&^%$#@!~"
ord_char_list = [ord(s) for s in chars]
print(ord_char_list)

# Comprehending Lists + Map, Filter
if_char_list = [ord(s) for s in chars if ord(s) > 40]
print(if_char_list)

filter_char_list = list(filter(lambda x: x > 40, map(ord, chars)))
print(filter_char_list)

# ord -> char
char_list = [chr(c) for c in ord_char_list]
print(char_list)

# 4-2. Generator
import array

# Generator : 한번에 한개의 항목을 생성(메모리 이점)
tuple_g = (ord(s) for s in chars)
print(tuple_g)
print(next(tuple_g))

array_g = array.array('I', (ord(s) for s in chars))
print(array_g)
print(array_g.tolist())

# Generator Example
students_g = ('%s' % c + str(n) for c in "ABCD" for n in range(1, 21))
print(students_g)
print(list(students_g))

# 리스트 주의 shallow copy vs deep copy
pass

