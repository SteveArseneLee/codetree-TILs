import sys
# 변수 선언 및 입력:
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
picked = []

ans = 0


# 현재 색칠된 칸을 선택할 행을 row라 했을 때
# 계속 탐색을 이어서 진행합니다.
# 첫 번째 행에 색칠할 열의 위치부터
# 두 번째, 세 번째, .. n번째 행에 색칠할 열의 위치까지
# 각 열의 위치에 대한 순열을 만들어줍니다.
def find_max(row):
    global ans

    # 색칠된 칸에 적힌 수들의 합 중
    # 최댓값을 갱신합니다.
    if row == n:
        min_val = sys.maxsize
        for i in range(n):
            min_val = min(min_val, grid[i][picked[i]])

        # 답을 갱신해줍니다.
        ans = max(ans, min_val)
        return

    # 현재 행에 색칠할 열을 선택합니다.
    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        picked.append(i)

        find_max(row + 1)

        visited[i] = False
        picked.pop()


# 합이 최대가 되도록
# 탐색을 진행합니다.
find_max(0)

print(ans)