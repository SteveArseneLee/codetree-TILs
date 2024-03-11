MAX_NUM = 10000
n, k = map(int, input().split())
pics = [list(input().split()) for _ in range(n)]

pics = sorted(pics, key=lambda x: int(x[0]))
# max_value = int(max(pics, key=lambda x: int(x[0]))[0])+1
max_value = int(pics[-1][0])
min_value = int(pics[0][0])
road = [0] * (max_value+1)

for i,j in pics:
    if j == 'G':
        road[int(i)] = 1
    elif j == 'H':
        road[int(i)] = 2
# print(road)
ans = 0
for i in range(min_value, MAX_NUM + 1 - k):
    ans = max(ans, sum(road[i:i+k+1]))
print(ans)