from collections import deque
n,k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited=[[False]*n for _ in range(n)]
cnt = 0

def can_go(x,y):
    return 0<=x<n and 0<=y<n and grid[x][y] == 0

dir = [(1,0),(-1,0),(0,1),(0,-1)]

q = deque()
def bfs(x,y):
    global cnt
    while q:
        x,y = q.popleft()
        for dx, dy in dir:
            nx,ny= x+dx,y+dy
            if can_go(nx, ny) and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
                cnt += 1

for _ in range(k):
    x,y = map(int, input().split())
    nx, ny= x-1, y-1
    q.append((nx,ny))
    bfs(nx,ny)
    # print(cnt)
print(cnt)