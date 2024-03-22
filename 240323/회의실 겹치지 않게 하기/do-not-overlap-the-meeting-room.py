n = int(input())
meetings = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:x[1])

last_e, max_cnt = -1, 0
for s,e in meetings:
    # 이전 회의와 겹치지 않으면 해당 회의 선택해줌
    if last_e <= s:
        last_e = e
        max_cnt += 1
print(n-max_cnt)