# ===========내 풀이==========
# a = list(input())
# if '0' not in a:
#     a[-1] = '0'
# else:
#     for i in range(len(a)):
#         if a[i] == '0':
#             a[i] = '1'
#             break

# x = ''.join(a)
# # print(type(x))
# print(int(x, 2))

# ========== 해설======
import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력
binary = list(map(int, list(input())))
length = len(binary)

# 각 i번째 자릿수를 바꾸었을 때의 십진수 값을 구해줍니다.
ans = INT_MIN
for i in range(length):
	# i번째 자릿수를 바꿉니다.
	binary[i] = 1 - binary[i]
	
	# 십진수로 변환합니다.
	num = 0
	for j in range(length):
		num = num * 2 + binary[j]
	
	ans = max(ans, num)
	
	# i번째 자릿수를 원래대로 돌려놓습니다.
	binary[i] = 1 - binary[i]

# 출력
print(ans)