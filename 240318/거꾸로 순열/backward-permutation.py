import sys
n = int(input())
selected = [0] * n
used = [0] * (n+1)
# print(selected, used)
def rec_func(k):
    # 종료조건
    if k == n:
        for x in selected:
            sys.stdout.write(str(x) + ' ')
        sys.stdout.write('\n')

    for cand in range(n,0,-1):
        if used[cand]: continue
        selected[k] = cand
        used[cand] = 1
        rec_func(k+1)
        selected[k] = 0
        used[cand] = 0
rec_func(0)