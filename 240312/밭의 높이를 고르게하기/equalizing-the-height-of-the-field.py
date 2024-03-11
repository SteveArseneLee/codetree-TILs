import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, h, t = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
   
# 모든 구간의 시작점을 잡아봅니다.
min_cost = INT_MAX
for i in range(n - t + 1):
    # 해당 구간을 고르게 할 때의 비용을 구합니다.
    cost = 0
    for j in range(i, i + t):
        cost += abs(arr[j] - h)
    
    # 최솟값을 구합니다.
    min_cost = min(min_cost, cost)

print(min_cost)