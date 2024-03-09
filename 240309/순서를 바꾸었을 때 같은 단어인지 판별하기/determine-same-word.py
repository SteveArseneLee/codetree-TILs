arr1 = list(input())
arr2 = list(input())
arr1.sort()
arr2.sort()
result = "Yes"
if arr1 != arr2:
    result = "No"
print(result)