# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"

print(len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon

print("""apple;orange;banana;lemon""")
print('apple','orange','banana','lemon', sep=';')


# 3. 화면에 * 기호 100개를 표시하세요.

print('*' * 100)


# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.

temp1 = "30"

print(int(temp1))
print(float(temp1))
print(complex(temp1))
print(str(temp1))

print("4. ", int("30"))
print("4. ", float("30"))
print("4. ", complex("30"))
print("4. ", str("30"))


# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.

temp1 = "Niceman"

print(temp1[4:])

#강사풀이
q5 = "Niceman"
q5_idx = q5.index("man")

print("5. ",q5_idx)
print("5. ",q5[q5_idx:q5_idx+3])
print("5. ",q5[4:7])


# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"

temp1 = "Strawberry"
print(temp1[::-1])

# 강사풀이
q6 = "Strawberry"

print("6  ", list(reversed(q6)))
print("6  ", q6[::-1])

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"

temp1 = "010-7777-9999"
print(temp1.replace("-",""))

# 강사풀이
q7 = "010-7777-9999"

print("7.   ", q7[0:3]+q7[4:8]+q7[9:13])

import re

print("7.   ", re.sub('[^0-9]','',q7))

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"

temp1 = "http://daum.net"
print(temp1.replace("http://",""))

# 강사풀이
q8 = "http://daum.net"

print("8.  ",q8[7:])

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"

temp1 = "NiceMan"
print("NiceMan".upper())
print("NiceMan".lower())

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"

temp1 = "abcdefghijklmn"

print(temp1[2:5])

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]

temp1 = ["Banana", "Apple", "Orange"]

temp1.remove("Apple")
print(temp1)

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)

# 튜플은 수정과 삭제가 안됨
temp1 = (1,2,3,4)

l = list(temp1)

print(l)


# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>

dict = {
    "성인" : 10000,
    "청소년" : 70000,
    "아동" : 30000
}

print(dict)

# 강사풀이 = 이렇게도 가능 함
q13 = {}
q13['성인'] = 10000
q13['청소년'] = 70000
q13['아동'] = 30000

print(q13)

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.

dict['소아'] = 0

print(dict)

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.

print(dict.keys())

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.

print(dict.values())
print(list(dict.values()))
print(tuple(dict.values()))

# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
