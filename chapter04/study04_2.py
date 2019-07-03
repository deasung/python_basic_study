# 문자열 및 연산자

# 문자열, 문자열 연산 , 슬라이싱
str1 = "I am Boy."
str2 = "Niceman"
str3 = ''
str4 = str('ace')


print(len(str1), len(str2), len(str3), len(str4))

# 이스케이프 문자

escape_str1 = "Do you have a \"big collection\""

print(escape_str1)

escape_str2 = "Tab \t Tat \t"
print(escape_str2)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)

raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인
multi = \
""" 
문자열 
멀티라인 
테스트 

"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = "def"
str_o4 = 'Niceman'


print(str_o1 * 100)
print(str_o2 + str_o3)  #같은 문자끼리 더할수 있고 곱할수 있다.
print(str_o1 * 3)
print('a' in str_o4)    #a라는 문자 str_o4에 포함되어 있으면 true/false로 반환
print('f' in str_o4)
print('z' not in str_o4)

# 문자열 형 변환
print(str(77))
print(str(77) + 'a')
print(str(10.4))

# 문자열 함수
# 참조 : https://www.w3schools.com/python/python_ref_string.asp