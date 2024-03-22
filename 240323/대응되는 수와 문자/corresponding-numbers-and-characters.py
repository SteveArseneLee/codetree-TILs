n,m = map(int,input().split())
arr = [input() for _ in range(n)]
for _ in range(m):
    tmp = input()
    # print(tmp)
    if tmp.isalpha():
        for i in range(n):
            if arr[i] == tmp:
                print(i+1)
    else: print(arr[int(tmp)-1])