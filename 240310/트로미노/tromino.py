n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0
shapes = [
    [[1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]],

    [[1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]],
]
def check(x,y):
    # 6가지의 경우를 따져보기
    max_sum = 0
    for i in range(6):
        is_possible=True
        sum_of_nums = 0
        for dx in range(0,3):
            for dy in range(0,3):
                if shapes[i][dx][dy] == 0:
                    continue
                if x+dx >= n or y + dy >= m:
                    is_possible = False
                else:
                    sum_of_nums += grid[x+dx][y+dy]
        if is_possible:
            max_sum = max(max_sum, sum_of_nums)
    return max_sum


for i in range(n):
    for j in range(m):
        # i,j번째의 최댓값 구하기
        ans = max(ans, check(i,j))
print(ans)