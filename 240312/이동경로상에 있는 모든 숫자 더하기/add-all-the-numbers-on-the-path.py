import sys
input = sys.stdin.readline
# n 크기의 정사각형 모양과 T개의 명령
n,t = map(int, input().split())
orders = list(input().rstrip())
grid = [list(map(int, input().split())) for _ in range(n)]

# 북쪽으로 시작해서 반시계로 써보자 북서남동
dx, dy = (-1,0,1,0),(0,-1,0,1)
dir = 0
ans = 0
x,y = n//2, n//2
selected = [grid[x][y]]
# print(x,y)
for order in orders:
    # print(order)
    # L은 왼쪽으로 90도 방향 전환
    if order == 'L':
        dir = (dir+1)%4
    # R은 오른쪽으로 90도 방향 전환
    elif order == 'R':
        dir = (dir+3)%4
    else:
        # print(order)
        # 이동할때 만약 같은 곳에 있으면 더하지는 않음
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0:
            x = 0
        elif nx >= n:
            x = n - 1
        else:
            x = nx

        if ny < 0:
            y = 0
        elif ny >= n:
            y = n - 1
        else:
            y = ny
        # print("x : ",x, " y: ", y)
        print(selected[-1])
        if selected[-1] != grid[x][y]: selected.append(grid[x][y])
print(sum(selected))