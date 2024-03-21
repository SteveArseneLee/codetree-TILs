import sys
n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)])
# 결과를 저장할 변수
min_length = float('inf')

for i in range(n):
    # i번째 선분을 제외한 나머지 선분들의 최소 시작점과 최대 종료점 찾기
    min_start = min(arr[j][0] for j in range(n) if j != i)
    max_end = max(arr[j][1] for j in range(n) if j != i)

    # i번째 선분을 제외했을 때의 선분 길이 계산
    length = max_end - min_start

    # 최소 길이 업데이트
    min_length = min(min_length, length)

print(min_length)