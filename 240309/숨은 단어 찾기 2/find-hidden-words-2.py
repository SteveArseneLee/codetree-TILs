n,m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
# print(arr)


# 'L'이 있다면 8가지 방향으로 확인
def check(i,j):
    ans = 0
    if i-2 >= 0 and arr[i-1][j] == arr[i-2][j] == 'E':
        ans += 1
    if i+2 < n and arr[i+1][j] == arr[i+2][j] == 'E':
        ans += 1

    if j-2 >= 0 and arr[i][j-1] == arr[i][j-2] == 'E':
        ans += 1
    if j+2 < n and arr[i][j+1] == arr[i][j+2] == 'E':
        ans += 1

    if i-2 >= 0 and j-2 >= 0 and arr[i-1][j-1] == arr[i-2][j-2] == 'E':
        ans += 1
    if i+2 < n and j+2 < n and arr[i+1][j+1] == arr[i+2][j+2] == 'E':
        ans += 1

    if i-2 >= 0 and j+2 < n and arr[i-1][j+1] == arr[i-2][j+2] == 'E':
        ans += 1
    if i+2 < n and j-2 >= 0 and arr[i+1][j-1] == arr[i+2][j-2] == 'E':
        ans += 1
    return ans

# print(arr)
result = 0
for i in range(n):
    for j in range(m):
        # print(arr[i][0])
        if arr[i][j] == 'L':
            result += check(i,j)

print(result)