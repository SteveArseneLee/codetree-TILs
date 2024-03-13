arr = ['L', 'E', 'B', 'R', 'O', 'S']
test = input()
# print(test, type(test))
if test not in arr:
    print("None")
else:
    for idx, item in enumerate(arr):
        if item == test:
            print(idx)