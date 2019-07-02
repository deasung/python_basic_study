# 파이썬 데이터 타입 종류
# Boolean
# Numbers
# String
# Bytes
# Lists
# Tuples
# Sets
# Dictionaries


# 데이터 타입

v_str1 = "Niceman"
v_bool = True #True 1 False 0
v_str2 = "Goodboy"
v_float = 10.3
v_dict = {
    "name" : "Kim",
    "age" : 25
}
v_list = [3,5,7]
v_tuple = 3, 5, 7
v_set = {7,8,9}

# type 자료형이 먼지 알려
print(type(v_tuple))
print(type(v_set))
print(type(v_float))

i1 = 39
i2 = 939
big_int1 = 999999999999999999999999999999999999999999999999
big_int2 = 777777777777777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2) #자동 형변환 실수 + 정수 = 실수

result = f3 + i2
print(result,type(result))

a = 5.
b = 4

print(type(a),type(b))

result2 = a + b
print(result2)

# 형변환
# int, float, complex(복소수)
print(int(result2))

# 정수 -> 실수
print(float(result2))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))

print(complex(False))

y = 100;
y = y + 100

y += 100

print(y)

# 수치 연산 함수
# https://docs.python.org/3/library/math.html

print(abs(-7))
#n, m = 10, 20

n, m = divmod(100,8)
print(n,m)

import math

print(math.ceil(5.1))
print(math.floor(3.874))

