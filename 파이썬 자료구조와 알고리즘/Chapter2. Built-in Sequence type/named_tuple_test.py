import collections

Person = collections.namedtuple('Person', 'name age gender') # 처음은 변수의 이름과 똑같이 사용, 이후 공백으로 구분하여 각 항목 지정
# Person = collections.namedtuple('Person', ['name', 'age', 'gender'])
# Person = collections.namedtuple('Person', ('name', 'age', 'gender')) # 셋 모두 결과가 같음

p = Person(name='아스틴', age=30, gender='남자')
print(p[0])
print(p.name)
print(p)
print('-' * 50)
# p.age = 20 -> 일반 튜플과 마찬가지로 불변형
for i in p:
    print(i)