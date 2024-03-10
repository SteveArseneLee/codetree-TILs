n = int(input())
xys = [list(map(int, input().split())) for _ in range(n)]
distance = 1000*1000*2
for x1 in xys:
    for x2 in xys:
        if x1 == x2: continue
        distance = min(distance, (x1[0] - x2[0])**2 + (x1[1] - x2[1])**2)
print(distance)