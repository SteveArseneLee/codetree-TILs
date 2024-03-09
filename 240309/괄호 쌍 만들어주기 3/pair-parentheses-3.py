test = list(input())
len_test = len(test)
# '('가 있는 위치에서 항상 테스트
def check(i):
    result = 0
    for x in range(i, len_test):
        if test[x] == ')':
            result += 1
    return result

cnt = 0
for i in range(len_test):
# for i in test:
    if test[i] == '(':
        cnt += check(i)
print(cnt)