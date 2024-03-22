n, m = map(int, input().split())
arr = list(map(int, input().split()))

freq = dict()

for elem in arr:
    if elem not in freq: freq[elem] =1
    else: freq[elem] += 1

queries = list(map(int, input().split()))
for num in queries:
    if num not in freq:
        print(0, end=' ')
    else:
        print(freq[num], end=' ')