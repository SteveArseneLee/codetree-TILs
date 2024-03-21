n, q = map(int, input().split())
arr = [[0,0,0] for _ in range(n+1)]
for i in range(1,n+1):
    rock = int(input())
    if rock == 1:
        arr[i][0] = arr[i-1][0] + 1
        arr[i][1] = arr[i-1][1]
        arr[i][2] = arr[i-1][2]
    elif rock == 2:
        arr[i][0] = arr[i-1][0]
        arr[i][1] = arr[i-1][1] + 1
        arr[i][2] = arr[i-1][2]
    else:
        arr[i][0] = arr[i - 1][0]
        arr[i][1] = arr[i - 1][1]
        arr[i][2] = arr[i-1][2] + 1
# print(arr)

def get_gap(s,e):
    a,b,c = arr[e][0]-arr[s-1][0],arr[e][1]-arr[s-1][1],arr[e][2]-arr[s-1][2]
    print(a,b,c)

for _ in range(q):
    s,e = map(int, input().split())
    get_gap(s,e)