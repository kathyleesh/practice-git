a = () # 이것이 바로 튜플이다
b = (1,) # 원소가 하나일때는 ,를 찍어줘야 튜플로 인식한다!
c = (11, 12, 13, 14)
d = (100, 1000,'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine')) # 튜플 안에 튜플도 중첩 선언이 가능하다

print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1]) # Captine으로 출력
print('e - ', e[-1][1]) # ('Ace', 'Base', 'Captine')에 첫번째이니깐 Base가 출력
print('e - ', list(e[-1][1])) # 튜플에서 리스트로 형변환

#튜플은 수정 불가능 #d[0] = 1500
#print('d - ', d)

print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

print('>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
# print("c[0] + 'hi' - ",c[0] + 'hi') # 튜플은 절대 never 수정,삭제가 안된다.
print("'Test' + c[0] - ", 'Test' + str(c[0])) # 따라서 수정하려면 형변환이 필요하다.

a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(5))
print('a - ', a.count(4))

t = ('foo', 'bar', 'baz', 'qux')

# 1
(x1, x2, x3, x4) = t # 소괄호가 있어도 없어도 언패킹이 되지만, 관습상 소괄호를 해줘야한다~

# 출력확인
print(type(x1), type(x2), type(x3), type(x4))
print(x1)
print(x2)
print(x3)
print(x4)

# 2
(x1, x2, x3, x4) = ('foo', 'bar', 'baz', 'qux')

# 출력 확인
print(type(x1), type(x2), type(x3), type(x4))
print(x1)
print(x2)
print(x3)
print(x4)

t2  = 1, 2, 3 # -> 따로 리스트나 자료형을 주지 않으면 자동으로 튜플로 팩킹이 된다.
t3 = 4, # -> 끝에 , 필수
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

# 출력 확인
print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)


