# import sys
# k,n = map(int, input().split())
# selected = [0 for _ in range(n)]

# def rec_func(x):
#     if x == n:
#         for t in selected:
#             sys.stdout.write(str(t) + ' ')
#         sys.stdout.write('\n')
#     else:
#         for i in range(1,k+1):
#             selected[x] = i
#             rec_func(x+1)
#             selected[x] = 0
# rec_func(0)
    
# ====== 해설 ======
# 변수 선언 및 입력
k, n = tuple(map(int, input().split()))
selected_nums = []


# 선택된 원소들을 출력해줍니다.
def print_permutation():
    for num in selected_nums:
        print(num, end = " ")
    print()


def find_permutations(cnt):
    # n개를 모두 뽑은 경우 답을 출력해줍니다.
    if cnt == n:
        print_permutation()
        return
    
    # 1부터 k까지의 각 숫자가 뽑혔을 때의 경우를 탐색합니다.
    for i in range(1, k + 1):
        selected_nums.append(i)
        find_permutations(cnt + 1)
        selected_nums.pop()


find_permutations(0)