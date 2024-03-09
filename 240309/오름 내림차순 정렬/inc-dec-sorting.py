import sys
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in arr:
    sys.stdout.write(i + ' ')
sys.stdout.write('\n')
arr.reverse()
for i in arr:
    sys.stdout.write(i + ' ')