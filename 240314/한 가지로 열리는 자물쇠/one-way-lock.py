n = int(input())
arr = list(map(int, input().split()))
# arr[i]과의 차가 2 이하인 애들만 골라봐
ans = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if abs(arr[0] - i ) <= 2 or abs(arr[1] - j) <= 2 or abs(arr[2]-k)<=2: ans+=1
print(ans)