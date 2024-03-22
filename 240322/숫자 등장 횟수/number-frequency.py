n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

for i in nums:
    print(arr.count(i), end=' ')