s, e = map(int, input().split())
ans = 0
for i in range(s,e+1):
    ans = max(ans, sum(list(map(int, str(i)))))
print(ans)