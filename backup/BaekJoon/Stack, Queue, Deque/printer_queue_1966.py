"""
    프린터 큐(https://www.acmicpc.net/problem/1966)
     - 인쇄 조건
      * 현재 Queue의 가장 앞에 있는 문서의 '중요도'를 확인
      * 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
        이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치, 그렇지 않다면 바로 인쇄
     - 입력 : 테스트케이스의 수
             문서의 개수 N(1 <= N <= 100),
                몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여있는지 나타내는 정수 M(0 <= M <= N)
                이때 맨 왼쪽은 0번째
             두 번째 줄에는 N개 문서의 중요도가 차례대로 주어미, 중요도는 1 이상 9 이하의 정수,
                중요도가 같은 무선서가 여러 개 있을 수도 있다
     - 출력 : 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력

     * 참고 : https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%801966%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%ED%94%84%EB%A6%B0%ED%84%B0-%ED%81%90
"""
from sys import stdin

for _ in range(int(stdin.readline().strip())):
    n, m = map(int, stdin.readline().split())
    priority = list(map(int, stdin.readline().split()))
    checkList = [0 for _ in range(n)]
    checkList[m] = 1 # 궁금한 문서 위치 저장

    count = 0
    while True:
        if priority[0] == max(priority):
            count += 1

            if checkList[0] != 1:
                del priority[0]
                del checkList[0]
            else:
                print(count)
                break
        else:
            priority.append(priority[0])
            checkList.append(checkList[0])
            del priority[0]
            del checkList[0]

