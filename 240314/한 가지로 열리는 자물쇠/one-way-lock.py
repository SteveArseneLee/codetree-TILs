# 변수 선언 및 입력
n = int(input())
a, b, c = tuple(map(int, input().split()))


# 모든 조합을 다 만들어 봅니다.
cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            # 한 자리라도 주어진 조합과의 거리가 2 이내인지 확인합니다.
            if abs(a - i) <= 2 or abs(b - j) <= 2 or \
               abs(c - k) <= 2:
                cnt += 1

print(cnt)