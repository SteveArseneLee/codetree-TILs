MAX_R = 200000

# 변수 선언 및 입력:
n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
checked = [0] * (MAX_R + 1)
ans = 0

# 주어진 좌표의 범위가 작을 때에는
# 배열을 이용하여 직접 각 칸에
# +1 -1을 진행해도 무방합니다.
for x1, x2 in segments:
    checked[x1] += 1
    checked[x2] -= 1

# 모든 곳을 조사해보며
# 그 중 가장 많이 겹치는 횟수를 구합니다.
# 겹치는 횟수는
# 각 위치에 적혀있는 숫자들의 합을 누적해주면 구해집니다.
overlapped_cnt = 0
for x in range(1, MAX_R + 1):
    overlapped_cnt += checked[x]
    ans = max(ans, overlapped_cnt)

print(ans)