test = list(input())
x,y = 0,0
# 앞으로 북서남동은 이걸로 고정
dx, dy = (0,-1,0,1),(1,0,-1,0)
dir_num = 0
for i in test:
    if i == 'L':
        dir_num = (dir_num+1)%4
    if i == 'R':
        if dir_num == 0: dir_num += 4
        dir_num = (dir_num-1)%4
    if i == 'F':
        x,y = x+dx[dir_num], y + dy[dir_num]
print(x,y)