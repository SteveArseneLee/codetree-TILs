n,m = map(int, input().split())
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

dx, dy = (0,1,0,-1),(1,0,-1,0)
dir = 0
ans = [[0] * m for _ in range(n)]

x,y = 0,0
ans[x][y] = 1
for i in range(2,n*m+1):
    # 현재 방향 기준으로 다음 위치 값 계산
    nx, ny = x + dx[dir], y + dy[dir]

    if not in_range(nx,ny) or ans[nx][ny] != 0:
        dir = (dir+1) % 4
    x, y = x + dx[dir], y + dy[dir]
    ans[x][y] = i

# 정답 출력
for i in range(n):
    for j in range(m):
        print(ans[i][j], end=' ')
    print()