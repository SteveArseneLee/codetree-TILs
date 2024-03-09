n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.sort()
arr2.sort()
result = "Yes"
for i in range(n):
    if arr1[i] != arr2[i]:
        result = "No"
print(result)