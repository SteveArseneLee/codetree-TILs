n,k,t = list(input().split())
arr = [input() for i in range(int(n))]
ans = [i for i in arr if t in i]
# print(ans)
ans.sort()
# print(ans)
print(ans[int(k)-1])