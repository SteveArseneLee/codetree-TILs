n,c,g,h = map(int, input().split())
centers = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[0],x[1]))
min_value = centers[0][0]
max_value = centers[-1][1]
def check(ta, tb, num):
    if num < ta: return c
    elif ta <= num <= tb: return g
    else: return h

ans = 0
for i in range(min_value, max_value+1):
    tmp = 0
    for x,y in centers:
        tmp += check(x,y,i)
    ans = max(ans, tmp)
print(ans)