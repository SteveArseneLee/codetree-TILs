from collections import deque

# 변수 선언 및 입력
n, k, u, d = tuple(map(int, input().split()))
a = [list(map(int, input().split()))  for _ in range(n)]

ans = 0

s_pos = []
pos = [(i, j) for i in range(n) for j in range(n)]

# bfs에 필요한 변수들 입니다.
q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y, target):
    if not in_range(x, y) or visited[x][y]:
        return False
    
    diff = abs(target - a[x][y])
    return u <= diff and diff <= d


def bfs():
    # queue에 남은 것이 없을때까지 반복합니다.
    while q:
        # queue에서 가장 먼저 들어온 원소를 뺍니다.
        x, y = q.popleft()
        
        dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

        # queue에서 뺀 원소의 위치를 기준으로 4방향을 확인해봅니다.
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            # 아직 방문한 적이 없으면서 갈 수 있는 곳이라면
            # 새로 queue에 넣어주고 방문 여부를 표시해줍니다. 
            if can_go(nx, ny, a[x][y]):
                q.append((nx, ny))
                visited[nx][ny] = True
                

def calc():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0
		
    # bfs를 이용해 k개의 시작점으로부터
    # 도달 가능한 지점을 탐색합니다.
    # 모든 시작점을 queue에 넣고 시작하면
    # 단 한번의 탐색 만으로 
    # 모든 도달 가능한 위치를 구할 수 있습니다.
    for x, y in s_pos:
        q.append((x, y))
        visited[x][y] = True
        
    bfs()
    
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1
                
    return cnt


def find_max(idx, cnt):
    global ans
    
    if cnt > k:
        return
    
    if idx == n * n:
        if cnt == k:
            ans = max(ans, calc())
        return
    
    s_pos.append(pos[idx])
    find_max(idx + 1, cnt + 1)
    s_pos.pop()
    
    find_max(idx + 1, cnt)


find_max(0, 0)
print(ans)