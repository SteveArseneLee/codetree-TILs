# ========== 내 풀이 =============
# n,k,t = list(input().split())
# len_t = len(t)
# arr = [input() for i in range(int(n))]
# ans = [i for i in arr if t in i[:len_t]]
# ans.sort()
# print(ans[int(k)-1])

# ======== 해설 ===========
# 변수 선언 및 입력
n, k, t = tuple(input().split())
n, k = int(n), int(k)


# a가 b로 시작하는지를 확인합니다.
def starts_with(a, b):
    # b의 길이가 더 길 수는 없습니다.
    if len(a) < len(b):
        return False
    
    # b의 길이만큼 살펴보며, a와 문자열이 완벽히 동일한지 확인합니다.
    return a[:len(b)] == b


words = []
for _ in range(n):
    word = input()
    if starts_with(word, t):
        words.append(word)

# 정렬을 진행합니다.
words.sort()

print(words[k - 1])