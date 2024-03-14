test_case = list(input())
x,y = 0,0
# 북, 동, 남, 서
dx, dy = (0,1,0,-1),(1,0,-1,0)
dir = 0
elapsed_time = 0
for i in test_case:
    if i == 'L':
        dir = (dir+1)%4
        elapsed_time += 1
    elif i == 'R':
        dir = (dir+3)%4
        elapsed_time += 1
    # F면 이동
    else:
        x,y = x+dx[dir], y+dy[dir]
        elapsed_time += 1
        # print(x,y)

    if x==0 and y==0:
        print(elapsed_time)
        break
if x!=0 and y!=0: print(-1)