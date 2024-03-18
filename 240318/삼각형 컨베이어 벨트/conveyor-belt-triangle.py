from collections import deque
# n개, t초 시간
n,t = map(int, input().split())
arr1 = deque(list(map(int, input().split())))
arr2 = deque(list(map(int, input().split())))
arr3 = deque(list(map(int, input().split())))

for _ in range(t):
    tmp1,tmp2,tmp3 = arr1[-1],arr2[-1],arr3[-1]
    arr1.rotate(1)
    arr2.rotate(1)
    arr3.rotate(1)
    arr1[0], arr2[0], arr3[0] = tmp3, tmp1, tmp2

for i in arr1:
    print(i, end=' ')
print()
for i in arr2:
    print(i, end=' ')
print()
for i in arr3:
    print(i, end=' ')