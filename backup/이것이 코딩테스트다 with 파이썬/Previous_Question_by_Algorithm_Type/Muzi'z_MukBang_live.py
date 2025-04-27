"""
    무지의 먹방 라이브
     - 각 음식에는 1부터 N까지의 번호가 붙어 있으며, 각 음식을 먹는데 일정 시간이 소요
      1. 무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓음
      2. 마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 옴
      3. 무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취
         다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식
      4. 회전판이 다음 음식을 무지 앞으로 가져오는 데 걸리는 시간은 없다고 가정
     - 무지가 먹방을 시작한 지 K초 후에 네트워크 장애로 방송이 잠시 중단
     - 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 먹어야 하는지 알고자 함
     - 각 음식을 모두 먹는데 필요한 시간이 담겨 있는 배열 food_times, 네트워크 장애가 발생한 시간 K초가 매개변수로 주어질 때
       몇 번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수를 완성하기
     - 정확성 테스트 제한 사항
            food_times 의 길이는 1 이상 2,000 이하이다.
            food_times 의 원소는 1 이상 1,000 이하의 자연수이다.
            k는 1 이상 2,000,000 이하의 자연수이다.
     - 효율성 테스트 제한 사항
            food_times 의 길이는 1 이상 200,000 이하이다.
            food_times 의 원소는 1 이상 100,000,000 이하의 자연수이다.
            k는 1 이상 2 x 10^13 이하의 자연수이다.
     - 입력 예시 : food_times = [3, 1, 2] / k = 5 -> result = 1
"""
import heapq
def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1

    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]

print(solution([3, 1, 2], 5))