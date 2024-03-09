import sys
from itertools import combinations
n, s = map(int, input().split())
arr = list(map(int, input().split()))

min_value = sys.maxsize
# 2개 제외한 합을 구하기
for i in combinations(arr, n-2):
    min_value = min(min_value, abs(sum(i)-s))
print(min_value)