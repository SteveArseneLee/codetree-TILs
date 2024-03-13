MAX_NUM = 3

# 변수 선언 및 입력
n = int(input())
commands = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

max_score = 0

# 시작 위치를 전부 가정해 봅니다.
# 그 중 최대 점수를 계산합니다.
for i in range(1, 4):
    # 종이컵을 전부 비워줍니다.
    yabawi = [0] * 4

    # i번째 종이컵에 처음 조약돌을 넣고 시작합니다.
    yabawi[i] = 1

    score = 0
    # 게임을 순서대로 진행합니다.
    for a, b, c in commands:
        # 두 종이컵을 교환합니다.
        yabawi[a], yabawi[b] = yabawi[b], yabawi[a]

        # 교환 이후 c번에 돌이 있다면 점수를 얻게 됩니다.
        if yabawi[c]:
            score += 1

    # 최대 점수를 갱신합니다.
    max_score = max(max_score, score)

print(max_score)