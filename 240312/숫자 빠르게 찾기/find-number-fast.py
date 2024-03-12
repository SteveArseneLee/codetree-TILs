n, m = map(int, input().split())
arr_n = tuple(map(int, input().split()))
arr_m = [int(input()) for _ in range(m)]
# for _ in range(m):
#     tmp = int(input())
#     print(tmp)
#     l, r = 0, n-1
#     idx = -1
#     while l <= r:
#         mid = (r - l + 1) // 2
# 
#         if arr_n[mid] == tmp:
#             idx = mid
#             break
#         if arr_n[mid] > tmp:
#             r = mid - 1
#         else:
#             l = mid + 1
#     print(idx) if idx == -1 else print(idx+1)

for target in arr_m:
    idx = -1
    l, r = 0, n-1
    while l <= r:
        mid = (l+r) // 2
        if arr_n[mid] == target:
            idx = mid
            break
        if arr_n[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    print(idx) if idx == -1 else print(idx+1)