x,y = map(int, input().split())

def check_interesting(x):
    tmp = list(map(int, str(x)))
    # print(tmp)
    set_tmp = list(set(tmp))
    # print(set_tmp)
    count_i, count_j = 0,0
    if len(set_tmp) != 2: return False
    else:
        i, j = set_tmp[0], set_tmp[1]
        for t in tmp:
            if t == i: count_i += 1
            else: count_j += 1
    return True if count_i == 1 or count_j == 1 else False

ans = 0
for i in range(x, y+1):
    if check_interesting(i): ans += 1
print(ans)