n = int(input())
cows = list(input())
c = []
o = []
w = []
for i in range(n):
    if cows[i] == 'C': c.append(i)
    elif cows[i] == 'O': o.append(i)
    else: w.append(i)
ans = 0
for x in c:
    for y in o:
        for z in w:
            if x < y < z: ans += 1
print(ans)