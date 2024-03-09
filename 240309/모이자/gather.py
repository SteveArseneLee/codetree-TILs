import sys
n = int(input())
arr = list(map(int, input().split()))
# arr.sort()
# test = sys.maxsize
test = []
for i in range(n):
    tmp = arr[i]
    value = 0
    for j in range(n):
        value += arr[j] * abs(i-j)
    # test = min(test, value)
    test.append(value)
print(min(test))