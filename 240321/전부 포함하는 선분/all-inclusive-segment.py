import sys
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = sys.maxsize
for i in range(n):
    tmp = arr[:i] + arr[i+1:]
    # print(tmp)
    tmp = sorted(tmp, key=lambda x: (x[0], x[1]))
    # print(tmp)
    ans = min(ans, tmp[-1][-1] - tmp[0][0])
print(ans)