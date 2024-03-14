# 변수 선언 및 입력
n = int(input())
arr = [
    input()
    for _ in range(n)
]

start_num = int(input())


# 주어진 숫자에 따라
# 시작 위치와 방향을 구합니다.
def initialize(num):
    if num <= n:
        return 0, num - 1, 0
    elif num <= 2 * n:
        return num - n - 1, n - 1, 1
    elif num <= 3 * n:
        return n - 1, n - (num - 2 * n), 2
    else:
        return n - (num - 3 * n), 0, 3

    
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n
    

# (x, y)에서 시작하여 next_dir 방향으로
# 이동한 이후의 위치를 반환합니다.
def move(x, y, next_dir):
    dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
    nx, ny = x + dxs[next_dir], y + dys[next_dir]
    return nx, ny, next_dir


def simulate(x, y, move_dir):
    move_num = 0
    while in_range(x, y):
        # 0 <-> 1 / 2 <-> 3
        if arr[x][y] == '/':
            x, y, move_dir = move(x, y, move_dir ^ 1)
        # 0 <-> 3 / 1 <-> 2
        else:
            x, y, move_dir = move(x, y, 3 - move_dir)
        
        move_num += 1
    
    return move_num
    

# 시작 위치와 방향을 구합니다.
x, y, move_dir = initialize(start_num)
# (x, y)에서 move_dir 방향으로 시작하여
# 시뮬레이션을 진행합니다.
move_num = simulate(x, y, move_dir)
print(move_num)