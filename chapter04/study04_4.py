
# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 딕셔너리 = 크롤링할떄 많이쓰임~~?

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key, Value (Json) -> MongoDB
# 선언
a = {'name': 'Kim', 'Phone': '010-7777-7777','birth': 870124}
b = {0: 'Hello Python',1: 'Hello Coding'}
c = {'arr': [1,2,3,4,5]}

print(type(a))


# 출력
print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)

a['rank'] = [1,3,4]
print(a)

a['rank2'] = (1,2,3,)
print(a)


# keys, values, items
print(a.keys())
# print(a.keys()[0]) #TypeError: 'dict_keys' object does not support indexing

print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

# print(a.values())

print()
print(list(a.values()))

print(a.items())

print()

print(list(a.items())) #리스트안에 튜플로 형변환

print(2 in b)
print('name2' in a)