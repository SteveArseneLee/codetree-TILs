n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()
# print(coins)

count = 0
for i in coins:
    count += k // i
    k %= i
print(count)