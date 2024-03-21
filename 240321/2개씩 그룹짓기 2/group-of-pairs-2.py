import sys
n = int(input())
arr = sorted(list(map(int, input().split())))

ans = sys.maxsize
for i in range(n):
    ans = min(ans, arr[n+i] - arr[i])
print(ans)