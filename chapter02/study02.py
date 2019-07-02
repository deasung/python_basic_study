# Section02-2

# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this
import sys


# 파이썬 기본 인코딩 python3 입력과 출력은 utf8
print(sys.stdin.encoding)
print(sys.stdout.encoding)


# 출력문
print('My name is Goodboy')

# 변수 선언
myName = 'GoodBoy'

# 조건문
if myName == "GoodBoy":
    print('Ok')


# 반복문
for i in range(1,10):
    for j in range(1,10):
        print('%d * %d = ' %(i,j), i*j)


# 파이썬 들여쓰기 자체도 문법 가독성이 좋다

# 변수 선언(한글) 권장하지않음
이름 = "좋은 사랑"

print(이름)

# 함수 선언(한글)
def 인사():
    print("안녕하세요.반값습니다.")

인사()

# 함수 선언(영문)
def greeting():
    print("hello!")

greeting()

# 클래스
class Cookie:
    pass


# 객체 생성
cookie = Cookie()


print(id(cookie))
print(dir(cookie))