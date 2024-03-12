MAX_A = 100

# 변수 선언 및 입력
n = int(input())

arr = list(map(int, input().split()))

ans = 0

# 각 숫자에 대해 
# 등차수열의 개수를 확인합니다.
for x in range(1, MAX_A + 1):
	# 모든 쌍을 만들어 등차수열의 개수를 확인합니다.
    cnt = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == 2 * x:
                cnt += 1

    ans = max(ans, cnt)
    
print(ans)