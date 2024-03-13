n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in range(n):
    for j in range(n-2):
        tmp = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        ans = max(tmp, ans)
print(ans)