n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
# print(grid)

def check_gold(x,y):
    num_of_gold = 0
    for row in range(x, x+3):
        for col in range(y, y+3):
            num_of_gold += grid[row][col]
    return num_of_gold

max_gold = 0
for i in range(n):
    for j in range(n):
        # 좌측 모서리를 기준으로 3*3개
        if i+2 >= n or j+2 >= n: continue
        else:
            gold_amount = check_gold(i,j)
            # print(gold_amount)
            max_gold = max(max_gold, gold_amount)
print(max_gold)