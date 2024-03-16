# 변수 선언 및 입력
n = int(input())
arr = list(map(int, input().split()))
numbers = [(num, i)  for i, num in enumerate(arr)]
answer = [0 for _ in range(n)]

# Custom Comparator를 활용한 정렬
numbers.sort(key=lambda x: (x[0], x[1]))
print(numbers)

# 정렬된 숫자들의 원래 인덱스를 활용한 정답 배열 저장
# 새로 저장된 인덱스, 값, 원래 인덱스
for i, (j, index) in enumerate(numbers):
    print("i: ",i, "j: ", j, "index: ", index)
    answer[index] = i + 1 # 인덱스 보정
    print(answer)

# 출력
for i in range(n):
    print(answer[i], end = ' ')