import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, s = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

array_sum = 0
ans = INT_MAX

# 배열의 값들의 총합을 미리 구해둡니다.
for elem in arr:
    array_sum += elem

# 모든 쌍을 다 잡아봅니다.
for i in range(n):
    for j in range(i + 1, n):
        # i번과 j번 수를 제외할 경우 남은 숫자들의 총합은 다음과 같습니다.
        new_sum = array_sum - arr[i] - arr[j]

        diff = abs(new_sum - s)
        ans = min(ans, diff)

# 정답을 출력합니다.
print(ans)