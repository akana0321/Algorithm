"""
    곱셈(https://www.acmicpc.net/problem/1629)
     - 입력 : A B C, 모두 2,147,483,647 이하의 자연수
     - 출력 : A를 B번 곱한 수를 C로 나눈 나머지 출력

     * 참고 : https://velog.io/@grace0st/%EA%B3%B1%EC%85%88-%EB%B0%B1%EC%A4%80-1629%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC
             https://somjang.tistory.com/entry/BaekJoon-1629%EB%B2%88-%EA%B3%B1%EC%85%88-Python
"""
from sys import stdin


def recursion_mutiply(a, b, c):
    if b == 1:
        return a % c
    else:
        temp = recursion_mutiply(a, b//2, c)
        if b % 2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c


a, b, c = map(int, stdin.readline().split())
print(recursion_mutiply(a, b, c))

# print(pow(a, b, c)) # 내장함수