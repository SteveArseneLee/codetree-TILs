import sys
si = sys.stdin.readline
n = int(input())
arr = list(map(int, si().split()))

val = arr[0]
for i in range(1, n):
    tmp = arr[i]
    if val < 0:
        val = max(tmp, val)
    else:
        val += tmp
print(val)