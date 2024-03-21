arr = sorted(list(map(int, input().split())))
# arr[-1]은 A+B+C
sum_value = arr[-1]
# arr[-2]는 B+C
a,b = sum_value - arr[-2], sum_value - arr[-3]
c = sum_value - a - b
# arr[-3]는 A+C
print(a,b,c)