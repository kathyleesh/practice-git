a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
# *주의* 키가 없이 리스트를 처럼 원소만 나열한다면 집합(Sets)이다!
# {}는 딕셔너리(Dictionary)에도 사용하지만 set에도 사용한다!!
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}

t = tuple(b)

print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

l = list(c)
l2 = list(e)

print('l - ', type(l), l)
print('l - ', l[0], l[1:3])
print('l2 - ', type(l2), l2)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2)) # intersection : 교집합

print('s1 | s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union(s2)) # union : 합집합

print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2)) # difference : 차집합

# 중복 원소 확인

print('s1 & s2 : ', s1.isdisjoint(s2)) # False가 나오면 교집합되는 원소가 있다는 뜻

# 교집합이 있으면 False, 없으면 True

# 부분 집합 확인
# 부분집합이란 집합 A의 모든 원소가 집합 B에 속할 때, A는 B의 부분집합이다.
# 상위집합이란 부분집합의 반대 개념

print('subset : ', s1.issubset(s2)) # issubset 함수를 통해서 부분집합인지 확인할 수 있다
print('superset : ', s1.issuperset(s2)) # issuperset 함수를 통해서 상위집합인지 확인할 수 있다

s1 = set([1, 2, 3, 4])

s1.add(5)

print('s1 - ', s1)

s1.remove(2)

print('s1 - ', s1)

# s1.remove(7) -> 에러 발생

s1.discard(3)

print('s1 - ', s1)

s1.discard(7) # discard는 예외가 발생하지 않는다. 따라서 가능하면 discard 사용

# 모두 제거

s1.clear()

print('s1 - ', s1)