n = int(input())
arr = [int(input()) for _ in range(n)]

sum_of_blocks = sum(arr)

# 평균 블럭 수 보다 큰 블럭에서만 차이를 옮겨준다.
avg = sum_of_blocks // n
# print(avg)
ans = 0
for block in arr:
    if block > avg:
        ans += block - avg

print(ans)