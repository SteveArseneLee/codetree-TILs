def max_positive_rectangle(grid):
    n, m = len(grid), len(grid[0])
    max_area = -1

    # 모든 가능한 직사각형에 대해
    for start_row in range(n):
        for start_col in range(m):
            for end_row in range(start_row, n):
                for end_col in range(start_col, m):
                    all_positive = True
                    # 직사각형 내 모든 값이 양수인지 확인
                    for i in range(start_row, end_row + 1):
                        for j in range(start_col, end_col + 1):
                            if grid[i][j] <= 0:
                                all_positive = False
                                break
                        if not all_positive:
                            break
                    
                    # 양수인 경우, 최대 크기 업데이트
                    if all_positive:
                        area = (end_row - start_row + 1) * (end_col - start_col + 1)
                        max_area = max(max_area, area)
    
    return max_area

# 입력 예시
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

print(max_positive_rectangle(grid))