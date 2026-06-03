n = int(input())
numbers = [0] + [int(input()) for _ in range(n)]

# Please write your code here.

# 연속하여 고른 수들의 합이 7의 배수가 되는 그룹들이 존재할 때, 그룹의 최대 크기를 구하라
# 연속하여 고른 수들이니까 슬라이딩 윈도우로 브루트 포스 수행
NUM = 7
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + numbers[i]

preprocess = [ele % NUM for ele in prefix]

remain_num = 6
answer = 0

def get_group_cnt(num):
    first_index = None
    last_index = None
    for i in range(n + 1):
        if preprocess[i] == num:
            first_index = i
            break
    
    for i in range(n, -1, -1):
        if preprocess[i] == num:
            last_index = i
            break
    
    if first_index is not None and last_index is not None and last_index >= first_index:
        return last_index - first_index
    return 0


for i in range(remain_num + 1):
    answer = max(answer, get_group_cnt(i))

print(answer)