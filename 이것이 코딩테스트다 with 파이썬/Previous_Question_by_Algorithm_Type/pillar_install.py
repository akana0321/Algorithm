"""
    기둥과 보 설치 https://programmers.co.kr/learn/courses/30/lessons/60061
     - 2차원 가상 벽면, 기둥과 보는 길이가 1
     - 기둥은 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나, 또는 다른 기둥 위에 있어야 함
     - 보는 한쪽 끝부분이 기둥 위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 함
     - 2차원 벽면은 n x n 크기, 각 격자는 1 x 1 크기
     - 맨 처음 벽면은 비어 있는 상태
     - 기둥과 보는 격자 선의 교차점에 걸치지 않고, 격자 칸의 각 변에 정확히 일치하도록 설치할 수 있음
     - 조건
        5 <= n <= 100
        1 <= bulid_frame의 세로 <= 1,000
        build_frame의 가로 = 4
        build_frame의 원소는 [x, y, a, b] 형태
         * x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표]
         * a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보
         * b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치
         * 벽면을 벗어나게 기둥, 보를 설치하는 경우는 없음
         * 바닥에 보를 설치하는 경우는 없음
        구조물은 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 or 삭제
        구조물이 겹치도록 설치하는 경우와 없는 구조물을 삭제하는 경우는 입력으로 주어지지 않음
        최종 구조물의 상태 return 규칙
         * return 하는 배열은 가로의 길이가 3인 2차원 배열로, 각 구조물의 좌표를 담고 있어야 함
         * 형식은 [x, y, z]
         * x, y는 기둥, 보의 교차점 좌표이며 [가로 좌표, 세로 좌표]
         * 기둥, 보는 교차점 좌표를 기준으로 오른쪽, 또는 위쪽 방향으로 설치되어 있음을 나타냄
         * a는 구조물의 종류를 나타내며, 0은 기둥, 1은 보
         * return 하는 배열은 x 좌표를 기준으로 오름차순, x 좌표가 같을 경우에는 y 좌표를 기준으로 오름차순
         * x, y 좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됨
"""


def impossible(answer):
    COL, ROW = 0, 1
    for x, y, a, in answer:
        if a == COL:  # 기둥일 때
            if y != 0 and (x, y - 1, COL) not in answer and \
                    (x - 1, y, ROW) not in answer and (x, y, ROW) not in answer:
                return True
        else:  # 보일 때
            if (x, y - 1, COL) not in answer and (x + 1, y - 1, COL) not in answer and \
                    not ((x - 1, y, ROW) in answer and (x + 1, y, ROW) in answer):
                return True
    return False


def solution(n, build_frame):
    answer = set()

    for x, y, a, build in build_frame:
        item = (x, y, a)
        if build: # 추가일 때
            answer.add(item)
            if impossible(answer):
                answer.remove(item)
        elif item in answer: # 삭제할 때
            answer.remove(item)
            if impossible(answer):
                answer.add(item)
    answer = map(list, answer)
    return sorted(answer)


n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
               [3, 2, 1, 1]]
print(solution(n, build_frame))
print()

n = 5
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
               [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
print(solution(n, build_frame))
