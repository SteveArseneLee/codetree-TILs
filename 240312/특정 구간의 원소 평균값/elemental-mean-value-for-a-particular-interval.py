# n개의 숫자
n = int(input())
arr = list(map(int, input().split()))
ans = 0
# 시작점과 끝점을 계속 잡아보기
for i in range(n):
    for j in range(i,n):
        if sum(arr[i:j+1])/(j-i+1) in arr[i:j+1]:
            # print("i:", i, " j:",j, arr[i:j+1], "mean:", sum(arr[i:j+1])/(j-i+1))
            ans += 1
print(ans)