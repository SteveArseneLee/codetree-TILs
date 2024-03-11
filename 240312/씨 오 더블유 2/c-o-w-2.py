# ============= 내 풀이 =============
# n = int(input())
# cows = list(input())
# c = []
# o = []
# w = []
# for i in range(n):
#     if cows[i] == 'C': c.append(i)
#     elif cows[i] == 'O': o.append(i)
#     else: w.append(i)
# ans = 0
# for x in c:
#     for y in o:
#         for z in w:
#             if x < y < z: ans += 1
# print(ans)

# ============== 해설 ===========
# 변수 선언 및 입력
n = int(input())
string = input()

# 모든 쌍을 다 잡아봅니다.
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if string[i] == 'C' and string[j] == 'O' and string[k] == 'W':
                cnt += 1

print(cnt)