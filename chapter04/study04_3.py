
# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트,튜플

# 리스트(순서o,중복o,수정o,삭제o)
# 선언

a = []
b = list() #명시적 사용가능
c = [1,2,3,4]
d = [10,100,'Pen','Banana','Orange']
e = [10,100,['Pen','Banana','Orange']]

# 인덱싱 문자열 한번 할당시 변경할수 없고 한글자한글자가 인덱스를 가지고 내부적으로 할당이 됨
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:2])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0])+'hi')

name1 = 'Lee'
name2 = 'Park'


# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100,1000,10000]
print(c)
c[1] = ['a','b','c']
print(c)


del c[1] #삭제하려는 인덱스 번호
print(c)

del c[-1]
print(c)

print()
print()

# 리스트 함수 조작 제어

y = [5,2,3,1,4]
print(y)

y.append(6)

print(y)

# y.sort()

print(y)

# y.reverse()

print(y)

y.insert(2,7)

print(y)

y.remove(2) #실제 값을 지움

y.remove(7)

print(y)

y.pop()
print(y)

ex = [88,77]
#y.append(ex) #현재 리스트 자체를 삽입
y.extend(ex) #끝부분 원소로 하나의 리스토로 출력
print(y)


# 삭제 : del, remove, pop


# 튜플 (순서o, 중복o, 수정x, 삭제x)

a = ()
b = (1,)
c = (1,2,3,4)

# del c[2] #TypeError: 'tuple' object doesn't support item deletion
d = (10,100,('a','b','c'))

print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])

print(c + d)
print(c * 3)

print()
print()

# 튜플 함수
z = (5,2,1,3,4)

print(z)
print(3 in z)
print(z.index(3)) #튜플중에 3이 있으면 boolean 
print(z.count(1)) #튜플중에 1이 몇개가 있는지