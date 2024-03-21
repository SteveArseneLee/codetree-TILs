from itertools import combinations

def valid_move(x, y, n):
    return 0 <= x < n and 0 <= y < n

def can_move(height1, height2, u, d):
    return u <= abs(height1 - height2) <= d

def dfs(grid, x, y, visited, u, d):
    n = len(grid)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    count = 1
    visited.add((x, y))

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if valid_move(nx, ny, n) and not (nx, ny) in visited:
            if can_move(grid[x][y], grid[nx][ny], u, d):
                count += dfs(grid, nx, ny, visited, u, d)

    return count

def max_cities(grid, k, u, d):
    n = len(grid)
    max_count = 0

    # 가능한 모든 시작 도시 조합을 확인
    for cities in combinations(range(n*n), k):
        count = 0
        visited = set()

        for city in cities:
            x, y = divmod(city, n)
            if not (x, y) in visited:
                count += dfs(grid, x, y, visited, u, d)

        max_count = max(max_count, count)

    return max_count

# 입력 받기
n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

print(max_cities(grid, k, u, d))