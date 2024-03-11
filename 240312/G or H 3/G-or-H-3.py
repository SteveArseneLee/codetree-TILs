# G와 H중 받은 알파벳의 팻말을 들고 있음
# 사진의 크기는 k
MAX_NUM = 10000
n, k = map(int, input().split())
pics = [list(input().split()) for _ in range(n)]

pics = sorted(pics, key=lambda x: int(x[0]))
# max_value = int(max(pics, key=lambda x: int(x[0]))[0])+1
max_value = int(pics[-1][0])
min_value = int(pics[0][0])
road = [0] * (max_value+1)
# print(min_value, max_value)
for i,j in pics:
    if j == 'G':
        road[int(i)] = 1
    elif j == 'H':
        road[int(i)] = 2
# print(road)
ans = 0
for i in range(MAX_NUM + 1 - k):
    # print("t: ", road[i:i+k+1])
    ans = max(ans, sum(road[i:i+k+1]))
print(ans)