n = int(input())
test_case = [tuple(input().split()) for _ in range(n)]
x, y = 0,0
dx, dy = [1,0,-1,0],[0,-1,0,1]
# dir_num = 2

for i in range(n):
    if test_case[i][0] == 'N':
        dir_num = 3
    elif test_case[i][0] == 'S':
        dir_num = 1
    elif test_case[i][0] == 'E':
        dir_num = 0
    elif test_case[i][0] == 'W':
        dir_num = 2

    x, y = x + int(test_case[i][1])*dx[dir_num],y + int(test_case[i][1])*dy[dir_num]
    # print(x,y)
print(x,y)