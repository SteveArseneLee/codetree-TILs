# 변수 선언 및 입력:

n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]


# (x1, y1), (x2, y2)를 두 꼭지점으로 하는
# 직사각형에 있는 값이 전부 양수인지 판단합니다.
def positive_rect(x1, y1, x2, y2):
    return all([
        grid[i][j] > 0
        for i in range(x1, x2 + 1)
        for j in range(y1, y2 + 1)
    ])


ans = -1

# 직사각형의 양쪽 두 꼭지점 (i, j), (k, l)
# 를 정하여
# 해당 직사각형안에 있는 값이 전부 양수일 때만
# 크기를 갱신합니다.
for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                if positive_rect(i, j, k, l):
                    ans = max(ans, (k - i + 1) * (l - j + 1))
print(ans)