def reflect(direction, mirror):
    if mirror == '/':
        return (direction - 1) % 4
    elif mirror == '\\':
        return (direction + 1) % 4

def simulate(grid, start, direction):
    n = len(grid)
    x, y = start
    count = 0

    while 0 <= x < n and 0 <= y < n:
        if grid[x][y] != ' ':
            direction = reflect(direction, grid[x][y])
            count += 1
        x += dx[direction]
        y += dy[direction]

    return count

N = int(input())
grid = [list(input()) for _ in range(N)]
K = int(input())

# 방향: 북, 동, 남, 서
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

# 시작 위치와 방향 설정
if K <= N:
    start = (0, K - 1)
    direction = 2  # 남쪽
elif K <= 2 * N:
    start = (K - N - 1, N - 1)
    direction = 3  # 서쪽
elif K <= 3 * N:
    start = (N - 1, 3 * N - K - 1)
    direction = 0  # 북쪽
else:
    start = (4 * N - K - 1, 0)
    direction = 1  # 동쪽

# 시뮬레이션 실행
result = simulate(grid, start, direction)
print(result)