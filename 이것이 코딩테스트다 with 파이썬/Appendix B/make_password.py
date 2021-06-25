'''
    암호는 서로 다른 L개의 알파벳 소문자들로 구성
    최소 한 개의 모음과 최소 두 개의 자음으로 구성
    암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열
    즉, xyz는 가능성이 있는 암호지만 yxz는 불가
    사용했을 법한 문자의 종류는 C가지
     - 두 정수 L, C가 주어진다 (3 <= L <= C <= 15)
     - C개의 문자들이 주어지며 공백으로 구분한다
     - 주어지는 문자들은 알파벳 소문자, 중복 X
     - 각 줄에 하나씩, 가능성 있는 암호를 모두 출력
'''
import itertools

vowels = ('a', 'e', 'i', 'o', 'u') # 5개의 모음 정의
l, c = map(int, input().split())

# 가능한 암호를 사전식으로 출력해야 하므로 입력 이후에 정렬 수행
array = input().split(' ')
array.sort()

# 길이가 l인 모든 암호의 조합 확인
for password in itertools.combinations(array, l):
    # 패스워드에 포함된 각 문자ㅡㄹ 확인하며 모음의 개수를 세기
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    # 최소 1개의 모음과 최소 2개의 자음이 있는 경우를 출력
    # if count >= 1 and count <= l - 2:
    if 1 <= count <= l - 2: # 위에를 이렇게 바꿀 수 있음
        print(''.join(password))
