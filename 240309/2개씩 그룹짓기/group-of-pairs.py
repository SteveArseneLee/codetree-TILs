n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# print(arr)
# 1, n
# 2, n-1
# 3, n-2
# ...
# n/2,
max_val = 0

for i in range(n):
    # print(arr[i], arr[-(i+1)])
    test = arr[i] + arr[-(1+i)]
    max_val = max(test, max_val)
print(max_val)