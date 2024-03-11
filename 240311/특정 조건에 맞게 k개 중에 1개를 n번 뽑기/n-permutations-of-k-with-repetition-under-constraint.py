# import sys
# n, m = map(int, sys.stdin.readline().split(' '))

# selected = [0 for _ in range(m)]
# used = [0 for _ in range(n + 1)]
# def rec_func(k):
#     if k == m:
#         for x in selected:
#             sys.stdout.write(str(x) + ' ')
#         sys.stdout.write('\n')
#     else:
#         for cand in range(1, n + 1):
#             if used[cand]:
#                 continue
#             if k>=2 and cand == selected[k-1] and cand == selected[k-2]: continue
#             selected[k] = cand
#             used[cand] = 1
#             rec_func(k + 1)
#             selected[k] = 0
#             used[cand] = 0

# rec_func(0)

# 변수 선언 및 입력
k, n = tuple(map(int, input().split()))
selected_nums = []


# 선택된 원소들을 출력해줍니다.
def print_permutation():
    for num in selected_nums:
        print(num, end = " ")
    print()


def find_duplicated_permutations(cnt):
    # n개를 모두 뽑은 경우 답을 출력해줍니다.
    if cnt == n:
        print_permutation()
        return
    
    for i in range(1, k + 1):
        if cnt >= 2 and i == selected_nums[-1] and i == selected_nums[-2]:
            continue
        else:
            selected_nums.append(i)
            find_duplicated_permutations(cnt + 1)
            selected_nums.pop()


find_duplicated_permutations(0)