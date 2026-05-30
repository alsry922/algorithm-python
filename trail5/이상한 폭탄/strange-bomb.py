import math
n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
MAX_K = 200001
# Please write your code here.
# 같은 수가 어느 위치에 나왔는지 보관
num_count = {}
for index, ele in enumerate(arr):
    if ele in num_count:
        num_count[ele].append(index)
    else:
        num_count[ele] = [index]

answer = -1
for key, value in num_count.items():
    # 같은 수가 두 번 이상 나오지 않았으면 건너뜀
    if len(value) < 2:
        continue
    length = len(value)
    bomb = False
    for i in range(length - 1):
        if abs(value[i] - value[i + 1]) <= k:
            bomb = True
            break

    if bomb:
        answer = max(answer, key)

print(answer)