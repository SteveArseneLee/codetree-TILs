import sys
k,n = map(int, input().split())
selected = [0 for _ in range(n)]

def rec_func(x):
    if x == n:
        for t in selected:
            sys.stdout.write(str(t) + ' ')
        sys.stdout.write('\n')
    else:
        for i in range(1,k+1):
            selected[x] = i
            rec_func(x+1)
            selected[x] = 0
rec_func(0)