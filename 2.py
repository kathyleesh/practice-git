# 데이터 타입
str1 = "Python"
str2 = 'Anaconda'
bool = True
float_v = 10.0 # 10 == 10.0는 틀린 것! int == float 이걸로 봐야한다.
int_v = 7
list = [str1, str2] # list는 대괄호 사용
dict = { # dict은 중괄호를 사용
    "name" : "Machine Learning",
    "version" : 2.0
}
tuple = (7, 8, 9) # tuple은 소괄호를 사용
set = {3, 5, 7} # set은 중괄호를 사용

# 정수 선언
i = 77
i2 = -14
big_int = 7777777777777777777777999999999999999999999999

# 정수 출력
print(i)
print(i2)
print(big_int)

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3/9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)

# 연산 데이터
i1 = 39
i2 = 939
big_int1 = 777777777777777777777799999999999999999999932334234
big_int2 = 434343434783478374838478374837434783473111111111111
f1 = 1.234
f2 = 3.939

# 덧셈
print(">>>>> + ")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)
print(i1 + f1)
print(f1 + i1)

# 뺄셈
print(">>>>> -")
print("i1 - i2: ", i1 - i2)
print("f1 - f2: ", f1 - f2)
print("big_int1 - big_int2: ", big_int1 - big_int2)
print()

# 곱셈
print(">>>>> *")
print("i1 * i2: ", i1 * i2)
print("f1 * f2: ", f1 * f2)
print("big_int1 * big_int2: ", big_int1 * big_int2)
print()

# 나눗셈
print(">>>>> /")
print("i2 / i1: ", i2 / i1)
print("f2 / f1: ", f2 / f1)
print("big_int2 / big_int1: ", big_int2 / big_int1)
print()

# 몫만 구하기
print(">>>>> //")
print("i2 // i1: ", i2 // i1)
print("f2 // f1: ", f2 // f1)
print("big_int2 // big_int1: ", big_int2 // big_int1)
print()

# 나머지 구하기
print(">>>>> %")
print("i1 % i2 :", i1 % i2)
print("f1 % f2 :", f1 % f2)
print("big_int1 % big_int2 :", big_int1 % big_int2)
print()

# n 제곱 구하기
print(">>>>> **")
print("2 ** 3: ", 2 ** 3)
print("i1 ** i2: ", i1 ** i2)
print("f1 ** f2: ", f1 ** f2)
print()

n = 10
f = 10.0

print(n==f)

# 형 변환 실습
a = 3
b = 6
c = .7
d = 12.7

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True : 1 , False : 0
print(float(False))
print(complex(3))
print(complex('3')) # 문자형 -> 숫자형
print(complex(False))

# 절대값 계산
print(abs(-7))

# 몫과 나머지 계산
x, y = divmod(100, 8)
print(x, y)

# n 제곱수 계산
print(pow(5,3), 5 ** 3)

import math

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수를 찾아주는 것
print(math.pi) # pi 값 제공

str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

# len 함수는 공백 포함해서 문자열의 길이를 알려준다.
print(len(str1), len(str2), len(str3), len(str4)) 

str1_t1 = ''
str1_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str1_t2), len(str1_t2))

escape_str1 = "Do you have a \"retro games\"?"
escape_str2 = 'What\'s on TV?'

# 출력1
print(escape_str1)
print(escape_str2)

t_s1 = "Click \tStart!"
t_s2 = "New Line\n Check!"

# 출력2
print(t_s1)
print(t_s2)

# 소문자 r가 붙으면 \를 있는 그대로 표시할 수 있다.
raw_s1 = r'D:\Python\python3' 
raw_s2 = r"\\x\y\z\q"

# Raw String 출력
print(raw_s1)
print(raw_s2)

str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3) # Python을 3번 반복해서 출력
print('=' * 50)
print(str_o1 + str_o2)
print('y' in str_o1) # y라는 알파벳이 str_o1에 있는지 확인해준다.
print('P' not in str_o2)

str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print("Capitalize: ", str_o1.capitalize()) # 첫번째 시작 문자를 대문자로 바꿔주는 함수
print("endswith: ", str_o2.endswith("s")) # 마지막 문자가 무엇인지 체크할때 사용하는 함수
print("join str: ", str_o1.join(["I'm ", "!"])) # 리스트에 특정 구분자를 추가하여 문자열을 변환하는 함수
print("replace1: ",str_o1.replace("thon", ' Good'))
print("replace2: ", str_o3.replace("are", "was"))
print("sorted: ", sorted(str_o1)) # 문자열을 입력받아 기준에 맞게 정렬한 후 리스트 형태로 반환하는 함수
print("split: ", str_o4.split(' ')) # 특정 단어를 분리할때, 단어 단위나 문장 단위로 분리할 때 많이 사용하는 함
print("reversed1: ", reversed(str_o2))
#print("reversed2: ", list(reversed(str_o2))) # list 형 변환

im_str = "Good Boy!"

# 출력
for i in im_str:
	print(i)

str_sl = "Nice Python"

# 슬라이싱 연습
print(str_sl[0:3]) # [start : end] []안에 시작과 끝 인덱스를 지정하면 해당 범위의 리스트를 잘라서 갖고온다.
# 주의할 점 end인덱스는 가져오려는 범위에 포함되지 않는다. 실제로 가져오려는 인덱스보다 1을 더 크게 지정한다.

print(str_sl[5:]) # str_sl[5:11]
print(str_sl[:len(str_sl)]) # str_sl[:11]이랑 같은것
print(str_sl[:len(str_sl)-1]) # str_sl[:10] 이니깐 0~9까지만 가져왔기때문에 'n'을 출력못함.
print(str_sl[1:9:2]) # [start:end:step] 몇개 단위로 점프(skip)하면서 가져올건지
print(str_sl[-5:]) # 음수가되면 오른쪽부터 출력된다.
print(str_sl[1:-2])
print(str_sl[::2]) # 처음부터 끝까지 2칸씩 간격으로 가져온다
print(str_sl[::-1]) # Nice Python이 역으로 출력된다.

# 중요 -> 음수는 오른쪽에서 왼쪽으로 일반적인 방향은 0부터 오른쪽으로

im_str = "Good Boy!"
print(dir(im_str)) # __iter__가 있으면 시퀀스를 반복할 수 있다는 것!