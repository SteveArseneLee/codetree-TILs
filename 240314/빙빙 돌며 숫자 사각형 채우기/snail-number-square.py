n,m = map(int, input().split())
def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

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


# n = 4
# answer = [[0] * n for _ in range(n)]
#
#
# def in_range(x, y):
#     return 0 <= x and x < n and 0 <= y and y < n
#
#
# dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
# x, y = 0, 0  # 시작은 (0, 0) 입니다.
# dir_num = 0  # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
#
# # 처음 시작 위치에 초기값을 적습니다.
# answer[x][y] = 1
#
# # n*n번 진행합니다.
# for i in range(2, n * n + 1):
#     # 현재 방향 dir를 기준으로 그 다음 위치 값을 계산합니다.
#     nx, ny = x + dxs[dir_num], y + dys[dir_num]
#
#     # 더 이상 나아갈 수 없다면
#     # 시계방향으로 90'를 회전합니다.
#     if not in_range(nx, ny) or answer[nx][ny] != 0:
#         dir_num = (dir_num + 1) % 4
#
#     # 그 다음 위치로 이동한 다음 배열에 올바른 값을 채워넣습니다.
#     x, y = x + dxs[dir_num], y + dys[dir_num]
#     answer[x][y] = i
#
# # 출력:
# for i in range(n):
#     for j in range(n):
#         print(answer[i][j], end=' ')
#     print()