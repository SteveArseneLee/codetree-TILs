a = list(input())
if '0' not in a:
    a[-1] = '0'
else:
    for i in range(len(a)):
        if a[i] == '0':
            a[i] = '1'
            break

x = ''.join(a)
# print(type(x))
print(int(x, 2))