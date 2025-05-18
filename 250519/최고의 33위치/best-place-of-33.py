n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_gold = 0

def get_num_of_gold(row_s, col_s, row_e, col_e):
    num_of_gold = 0

    for row in range(row_s, row_e + 1):
        for col in range(col_s, col_e + 1):
            num_of_gold += grid[row][col]
    return num_of_gold

for i in range(n-2):
    for j in range(n-2):
        num_of_gold = get_num_of_gold(i,j,i+2,j+2)

        max_gold = max(max_gold, num_of_gold)

print(max_gold)

# n = int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]

# # 2차원 prefix sum 배열 생성 (1-indexed)
# prefix = [[0] * (n + 1) for _ in range(n + 1)]

# # 누적합 계산
# for i in range(n):
#     for j in range(n):
#         prefix[i + 1][j + 1] = (
#             grid[i][j]
#             + prefix[i][j + 1]
#             + prefix[i + 1][j]
#             - prefix[i][j]
#         )

# # 3x3 격자에서 최대 동전 개수 구하기
# max_gold = 0
# for i in range(n - 2):      # 3x3 시작점: row
#     for j in range(n - 2):  # 3x3 시작점: col
#         r1, c1 = i, j
#         r2, c2 = i + 2, j + 2

#         # (r1,c1) ~ (r2,c2)의 합
#         total = (
#             prefix[r2 + 1][c2 + 1]
#             - prefix[r1][c2 + 1]
#             - prefix[r2 + 1][c1]
#             + prefix[r1][c1]
#         )

#         max_gold = max(max_gold, total)

# print(max_gold)
