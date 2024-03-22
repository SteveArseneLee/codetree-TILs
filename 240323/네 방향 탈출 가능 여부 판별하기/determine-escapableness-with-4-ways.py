import sys
from collections import deque
n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]
def in_range(x,y): return 0<=x<n and 0<=y<m
def can_go(x,y): return in_range(x,y) and not visited[x][y] and grid[x][y]

q = deque()
dir = [(-1,0),(1,0),(0,1),(0,-1)]
def bfs():
    while q:
        x,y = q.popleft()
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if can_go(nx,ny):
                q.append((nx,ny))
                visited[nx][ny] = True

q.append((0,0))
visited[0][0] = True

bfs()
print(0) if not visited[n-1][m-1] else print(1)