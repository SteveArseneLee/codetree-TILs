import sys
n,m = map(int, input().split())
selected=[]
used=[False]*(n+1)
ans = []
def rec_func(start_num, k):
    if start_num == n+1:
        if k == m:
            for i in selected:
                print(i, end=' ')
            print()
        return
    selected.append(start_num)
    rec_func(start_num+1, k+1)
    selected.pop()
    rec_func(start_num+1, k)

rec_func(1,0)