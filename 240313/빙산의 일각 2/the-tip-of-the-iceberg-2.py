MAX_H = 1000

# 변수 선언 및 입력
n = int(input())

h = [
    int(input())
    for _ in range(n)
]

ans = 0

# 각 높이에 대해
# 빙산 덩어리의 개수의 최댓값을 구합니다.
for i in range(1, MAX_H):
	# 물의 높이가 i일때 빙산 덩어리의 개수를 구합니다.
    cnt = 0

    # 가장 왼쪽에 빙산이 있는 경우의 예외를 처리해줍니다.
    if h[0] > i:
        cnt += 1

    # 바로 앞 블록은 해수면에 잠겨있고
    # 자기 자신의 블록은 해수면 위에 떠있는 경우,
    # 자기 자신 블록부터 시작하는 빙산이 하나 더 있습니다.
    for j in range(1, n):
        if h[j] > i and h[j - 1] <= i:
            cnt += 1

    ans = max(ans, cnt)
    
print(ans)