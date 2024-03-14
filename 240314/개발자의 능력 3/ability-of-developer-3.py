import sys
arr=list(map(int,input().split()))
ans = sys.maxsize
def get_team(i,j,k):
    team1 = arr[i] + arr[j] + arr[k]
    team2 = sum(arr) - team1
    return abs(team1 - team2)
for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            ans = min(ans, get_team(i,j,k))
print(ans)