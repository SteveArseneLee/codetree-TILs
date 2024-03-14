# 변수 선언 및 입력
dirs = input()
x, y = 0, 0
curr_dir = 3

# 동, 남, 서, 북 순으로 dx, dy를 정의합니다.
dxs = [1,  0, -1, 0];
dys = [0, -1,  0, 1];

# flag : 시작점으로 되돌아 왔는지 여부
flag = False;

leng = len(dirs)

# 움직이는 것을 진행합니다.
for i in range(leng):
	c_dir = dirs[i]
	# 반시계방향 90' 회전
	if c_dir == 'L':
		curr_dir = (curr_dir - 1 + 4) % 4
	# 시계방향 90' 회전
	elif c_dir == 'R':
		curr_dir = (curr_dir + 1) % 4
	# 직진
	else:
		x, y = x + dxs[curr_dir], y + dys[curr_dir]
	
	# 시작점으로 되돌아왔을 때
	if x == 0 and y == 0:
		print(i + 1)
		flag = True
		break
	
# 시작점으로 되돌아오지 못했을 때
if flag == False:
	print(-1)