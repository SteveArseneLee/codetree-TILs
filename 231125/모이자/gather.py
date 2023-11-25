import sys
n = int(input())
arr = list(map(int, input().split()))

# print(n, arr)
min_dist = sys.maxsize
for i in range(n):
    sum_dist = 0
    for j in range(n):
        sum_dist += abs(j-i) * arr[j]
    
    min_dist = min(min_dist, sum_dist)
print(min_dist)