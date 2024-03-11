def min_cost_to_even_heights(N, H, T, heights):
    min_cost = float('inf')

    for i in range(N - T + 1):
        cost = 0
        for j in range(i, i + T):
            if heights[j] < H:
                cost += H - heights[j]
            elif heights[j] > H:
                cost += heights[j] - H

        min_cost = min(min_cost, cost)

    return min_cost

# 입력 받기
N, H, T = map(int, input().split())
heights = list(map(int, input().split()))

# 최소 비용 계산
result = min_cost_to_even_heights(N, H, T, heights)

# 결과 출력
print(result)