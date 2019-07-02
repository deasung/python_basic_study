
# Print 구문
# 기본출력
print('Hello Python!')
print("Hello")
print("""Hello""")
print('''Hello''')


print() #원하는 출력값 없으면 구분


# Separator 옵션 사용

print('T','E','S','T', sep='')
print('2019','02','19', sep='-')
print('niceman','google.com',sep='@')

# end 옵션 사용
print('Welcome To', end=' ')
print(' the black parade', end=' ')
print('piano notes')

# format 사용 [],{},()
print('{} and {}'.format('You','Me'))

# 숫자 할당 가능 패턴
print("{0} and {1} and {0}".format('You','Me'))
print("{a} are {b}".format(a='You',b='Me'))

print("%s's favorite number is %d" % ('Enuki',7)) # %s : 문자, %d : 정수, %f : 실수

# 자리수 지정
print("Test1: %5d, Price: %4.2f" %(776,6534.123))
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(776,6534.123))
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=776,b=6534.123))

#
print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\\n')
print('test')
print('\t\t\ttest')