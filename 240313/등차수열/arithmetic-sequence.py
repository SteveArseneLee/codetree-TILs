n = int(input())
nums = sorted(list(map(int, input().split())))
ans = 0

def check(x,y,k):
    return True if k-x == y-k else False
for k in range(min(nums), max(nums) + 1):
    # k랑 nums의 숫자 두개가 등차수열인 개수 세기
    # print(k)
    tmp = 0
    for i in range(n):
        for j in range(i+1,n):
            if check(nums[i],nums[j],k):
                # print(nums[i],nums[j],k)
                tmp += 1
    ans = max(ans,tmp)
print(ans)