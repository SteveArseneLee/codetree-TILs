n = int(input())
zenga = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

def work(x,y):
    tmp = zenga[y:]
    return zenga[:x-1] + tmp

zenga = work(s1, e1)
zenga = work(s2, e2)
print(len(zenga))
if len(zenga) > 0:
    for i in zenga: print(i)