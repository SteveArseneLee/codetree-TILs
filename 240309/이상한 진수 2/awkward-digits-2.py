a = list(input())
for i in range(len(a)):
    if a[i] == '0':
        a[i] = '1'
        break

x = ''.join(a)
# print(type(x))
print(int(x, 2))