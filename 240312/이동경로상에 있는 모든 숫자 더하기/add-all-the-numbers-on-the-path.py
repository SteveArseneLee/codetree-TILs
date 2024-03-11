# n 크기의 정사각형 모양과 T개의 명령
n, t = map(int, input().split())
orders = list(input().rstrip())
grid = [list(map(int, input().split())) for _ in range(n)]

# 북쪽으로 시작해서 반시계로 써보자 북서남동
dx, dy = (-1, 0, 1, 0), (0, -1, 0, 1)
dir = 0
ans = 0
x, y = n // 2, n // 2
ans += grid[x][y]

for order in orders:
    if order == 'L':
        dir = (dir + 1) % 4
    elif order == 'R':
        dir = (dir + 3) % 4
    else:
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n:
            x, y = nx, ny
            ans += grid[x][y]

print(ans)