# 1이상 4이하의 숫자로만 이루어져있어서 되는 걸 만들어서 숫자세기
# 1~4 사이의 숫자 중 하나를 선택해 총 N번 선택하는 재귀로 가능한 모든 숫자들을 만들어냄
n = int(input())
ans = 0
seq = []

def is_beautiful():
    # 연달아 같은 숫자가 나오는 시작 위치를 잡기
    i = 0
    while i < n:
        # 만약 연속해서 해당 숫자만큼 나올 수 없으면
        # 아름다운 수가 아님
        if i + seq[i] - 1 >= n:
            return False
        # 연속해서 해당 숫자만큼 같은 숫자가 있는지 확인
        # 하나라도 다른 숫자가 있으면
        # 아름다운 수가 아님
        for j in range(i, i+seq[i]):
            if seq[j] != seq[i]: return False
        
        i += seq[i]
    return True

def count_beautiful_seq(cnt):
    global ans
    if cnt == n:
        if is_beautiful():
            ans+=1
        return
    for i in range(1,5):
        seq.append(i)
        count_beautiful_seq(cnt + 1)
        seq.pop()
count_beautiful_seq(0)
print(ans)