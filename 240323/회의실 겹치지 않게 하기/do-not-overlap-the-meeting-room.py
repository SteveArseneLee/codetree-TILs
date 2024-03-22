def schedule_meetings(meetings):
    # 회의를 종료 시간 기준으로 정렬
    meetings.sort(key=lambda x: x[1])
    
    count = 0
    end_time = -1
    
    for start, end in meetings:
        if start >= end_time:
            end_time = end
        else:
            count += 1

    return count

# 입력
n = int(input("회의의 개수를 입력하세요: "))
meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 최소 취소 회의 수 계산
min_cancellations = schedule_meetings(meetings)

# 출력
print(min_cancellations)