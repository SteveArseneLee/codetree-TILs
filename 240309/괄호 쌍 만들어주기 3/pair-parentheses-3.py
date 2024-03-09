# test = list(input())
# len_test = len(test)
# # '('가 있는 위치에서 항상 테스트
# def check(i):
#     result = 0
#     for x in range(i, len_test):
#         if test[x] == ')':
#             result += 1
#     return result

# cnt = 0
# for i in range(len_test):
# # for i in test:
#     if test[i] == '(':
#         cnt += check(i)
# print(cnt)

# 변수 선언 및 입력
string = input()
n = len(string)

# 모든 쌍을 다 잡아봅니다.
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if string[i] == '(' and string[j] == ')':
            cnt += 1
            
print(cnt)