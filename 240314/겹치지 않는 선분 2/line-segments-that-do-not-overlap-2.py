# 변수 선언 및 입력
n = int(input())
x = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = 0


# 다른 선분과 겹치지 않는 선분의 수를 구합니다.
for i in range(n):
	# i번째 선분이 다른 선분과 겹치지 않는지 확인합니다.
	overlap = False
	
	for j in range(n):
		# 자기 자신은 제외합니다.
		if j == i:
			continue
		
		# x1이 큰 쪽이 x2가 더 작다면 겹치게 됩니다.
		if (x[i][0] <= x[j][0] and x[i][1] >= x[j][1]) or (x[i][0] >= x[j][0] and x[i][1] <= x[j][1]):
			overlap = True
			break
	
    # 겹치지 않았다면 정답의 개수에 하나를 추가합니다.
	if overlap == False:
		ans += 1

print(ans)