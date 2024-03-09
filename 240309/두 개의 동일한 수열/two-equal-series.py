n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = "No"
for i in range(n):
    if arr1[i] == arr2[i]:
        continue
    result = "Yes"
print(result)