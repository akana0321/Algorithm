'''
    순열 : 서로 다른 n개에서 r개를 선택하여 일렬로 나열하는 것
    조험 : 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것

    itertools를 사용한다
'''

import itertools

data = [1, 2]

for x in itertools.permutations(data, 2):
    print(list(x))

data = [1, 2, 3]

for x in itertools.combinations(data, 2):
    print(list(x), end=' ')

