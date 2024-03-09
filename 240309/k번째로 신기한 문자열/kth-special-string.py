n,k,t = list(input().split())
len_t = len(t)
# print(len_t)
arr = [input() for i in range(int(n))]
ans = [i for i in arr if t in i[:len_t]]
# print(ans)
ans.sort()
# print(ans)
print(ans[int(k)-1])