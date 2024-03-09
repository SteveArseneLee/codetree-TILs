# n과 t(시간)
n,t = map(int, input().split())
up_belt = list(map(int, input().split()))
down_belt = list(map(int, input().split()))

for _ in range(t):
    temp_up = up_belt[n-1]
    for i in range(n-1,0, -1):
        up_belt[i] = up_belt[i-1]
    up_belt[0] = down_belt[n-1]
    for i in range(n-1,0,-1):
        down_belt[i] = down_belt[i-1]
    down_belt[0] = temp_up

for i in up_belt:
    print(i, end= ' ')
print()
for i in down_belt:
    print(i, end= ' ')