import sys
n,m = map(int, input().split())
selected=[0] * m
used=[False]*(n+1)
ans = []
def rec_func(k):
    if k == m:
        ans.append(selected[:])
    else:
        for cand in range(1,n+1):
            if not used[cand]:
                selected[k] = cand
                used[cand] = True
                rec_func(k+1)
                selected[k] = 0
                used[cand] = False

rec_func(0)
real_ans = []
for i in ans:
    i.sort()
    if i not in real_ans:
        real_ans.append(i)
for i in real_ans:
    for j in i:
        print(j,end=' ')
    print()