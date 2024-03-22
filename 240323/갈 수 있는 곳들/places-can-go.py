from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

q = deque()
def in_range(x,y): return 0 <=x<n and 0<=y<n
def can_go(x,y): return in_range(x,y) and not visited[x][y] and not grid[x][y]

def bfs():
    while q:
        x,y = q.popleft()
        dxs, dys = [0,0,-1,1],[1,-1,0,0]

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y+dy
            if can_go(new_x,new_y):
                q.append((new_x, new_y))
                visited[new_x][new_y] = True

for _ in range(k):
    x, y= tuple(map(int, input().split()))
    q.append((x-1, y-1))
    visited[x-1][y-1] = True

bfs()

ans = sum([
    1
    for i in range(n)
    for j in range(n)
    if visited[i][j]
])
print(ans)