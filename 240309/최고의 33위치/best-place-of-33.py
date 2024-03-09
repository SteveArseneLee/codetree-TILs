# 변수 선언 및 입력
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


# (row_s, col_s) ~ (row_e, col_e) 사이의 금의 개수를 계산합니다.
def get_num_of_gold(row_s, col_s, row_e, col_e):
    num_of_gold = 0

    for row in range(row_s, row_e + 1):
        for col in range(col_s, col_e + 1):
            num_of_gold += grid[row][col]

    return num_of_gold


max_gold = 0

# (row, col)이 3 * 3 격자의 좌측 상단 모서리인 경우를 전부 탐색합니다. 
for row in range(n):
    for col in range(n):
        # 3 * 3 격자가 n * n 격자를 벗어나는 경우는 계산하지 않습니다.
        if row + 2 >= n or col + 2 >= n:
            continue
        
        num_of_gold = get_num_of_gold(row, col, row + 2, col + 2)
            
        # 최대 금의 개수를 저장합니다.
        max_gold = max(max_gold, num_of_gold)

print(max_gold)