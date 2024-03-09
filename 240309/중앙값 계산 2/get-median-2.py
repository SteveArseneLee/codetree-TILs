n = int(input())
arr = list(map(int, input().split()))
ans = []
for i in range(1,n+1):
    # 홀수면
    if i%2 != 0:
        tmp = arr[:i]
        tmp.sort()
        ans.append(tmp[i//2])
for i in ans:
    print(i, end=' ')