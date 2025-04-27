"""
    문자열 압출
     - 연속된 문자를 압축하여 출력
     - 입력 : s는 소문자로, 길이는 1이상 1,000 이하
     - 출력 : 1개 이상의 단위로 압축하여 표현한 문자열 중 가장 짧은 것의 길이

    ** if문 한 줄에 쓰기
     - 기존
        if a > b:
            print(a)
        else:
            print(b)
     - 한 줄에 쓰기
        print(a if a > b else b)
"""
def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[:step]
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수 증가
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer