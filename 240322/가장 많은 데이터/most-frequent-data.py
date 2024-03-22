n = int(input())
arr = {}
ans = 0
for _ in range(n):
    tmp = input()
    # get 메서드를 사용하여 키가 없을 경우 기본값 0을 반환
    if tmp not in arr: arr[tmp] = 1
    else: arr[tmp] += 1
    ans = max(ans, arr[tmp])
print(ans)