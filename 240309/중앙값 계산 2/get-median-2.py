n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    # 홀수면
    if (arr[i]%2) != 0:
        # i번째까지 출력
        # print(arr[:i+1])
        print(arr[(i+1)//2])