from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited=[[False for _ in range(m)] for _ in range(n)]

q = deque()

def in_range(x,y): return 0 <= x < n and 0<=y<m

# 주어진 위치로 이동가능한지
def can_go(x,y): return in_range(x,y) and grid[x][y] and not visited[x][y]

def bfs():
    # queue에 남은게 없을때까지 반복
    while q:
        x,y = q.popleft()
        dxs, dys = [0,1,0,-1], [1,0,-1,0]
        for dx, dy in zip(dxs,dys):
            new_x, new_y = x+dx, y+dy
            # 아직 방문하지 않았으면서 갈수 있으면 새로 queue에 넣어주고 방문으로 변경
            if can_go(new_x, new_y):
                q.append((new_x, new_y))
                visited[new_x][new_y] = True

q.append((0,0))
visited[0][0] = True

bfs()

print(1) if visited[n-1][m-1] else print(0)