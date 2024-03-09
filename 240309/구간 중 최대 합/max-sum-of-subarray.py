import sys
si = sys.stdin.readline
n, k = map(int, si().split())
arr = list(map(int, si().split()))

result = 0
for i in range(n-k+1):
    result = max(result, sum(arr[i:i+3]))
print(result)