str1 = input()
str2 = input()

# 각 문자열을 정렬했을 때 두 문자열이 일치하는지 비교합니다.
print("Yes" if sorted(str1) == sorted(str2) else "No")