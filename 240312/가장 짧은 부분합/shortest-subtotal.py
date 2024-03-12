import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, s = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))


# 가능한 구간 중 가장 짧은 길이를 구합니다.
ans = INT_MAX

# 구간을 잡아봅니다.
sum_val = 0
j = 0
for i in range(1, n + 1):
    # 구간 내 합이 s보다 작으면 계속 진행합니다.
    while j + 1 <= n and sum_val < s:
        sum_val += arr[j + 1]
        j += 1

    # 만약 최대한 이동했는데도
    # sum_val이 s가 되지 못했다면
    # 탐색을 종료합니다.
    if sum_val < s:
        break
    
    # 현재 구간 [i, j]는 
    # i를 시작점으로 하는
    # 가장 짧은 구간이므로
    # 구간 크기 중 최솟값을 갱신합니다.
    ans = min(ans, j - i + 1)

    # 다음 구간으로 넘어가기 전에
    # arr[i]에 해당하는 값은 구간에서 제외시킵니다.
    sum_val -= arr[i]

# 만약 불가능하다면
# -1을 답으로 합니다.
if ans == INT_MAX:
    ans = -1

print(ans)