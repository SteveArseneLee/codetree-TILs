n,k,t = list(input().split())
arr = [input() for i in range(int(n))]
arr.sort()
cnt = 0
for i in arr:
    if t in i:
        # print("yes")
        cnt += 1
        # print(cnt)
        # print(i)
        if cnt == int(k):
            print(i)
            break