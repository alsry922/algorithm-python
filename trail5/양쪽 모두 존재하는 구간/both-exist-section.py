n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
# 1이상 M이하의 숫자가 적어도 하나씩 구간 안에 존재하고,
# 구간 밖에도 존재하는 가장 짧은 구간의 길이를 출력
# 구간을 잡아서 문제 풀이 -> 슬라이딩 윈도우
# 가장 짧은 구간 찾기 -> 가변 윈도우
# 투 포인터 사용 가능?
#   i, j 포인터 잡았을 때,
#   i를 증가시키면 1 ~ M 이하의 숫자 중 하나가 없어짐.
#   이로 인해 조건을 만족하지 않게 되면 j 또한 증가시켜,
#   조건을 만족시킬 수 있도록 수를 탐색해야함.
#   따라서, i, j 모두 한 방향으로만 움직임. -> 단조성 확인

# 배열 내의 모든 수 등장 횟수를 count하여 저장.(out_count dict)
# 구간 안에서 1 ~ M 이하의 등장 횐수를 count하여 저장.(in_count dict)
# i ~ M 이하의 숫자 중 몇 가지의 숫자가 있는지 변수로 저장.(out_condition, in_condition)
# 이 변수는 특정 숫자가 0이 되거나, 0 -> 1로 증가하는 경우 +- 1 연산을 해서 계산함.

# j + 1 위치의 수를 뽑을 수 있는지 반복 확인
#   j + 1 위치가 범위를 벗어나면 암됨
#   j + 1 위치의 수가 in_count 안에 이미 있는 경우
#       뽑을 수 있음
#   j + 1 위치의 수가 in_count 안에 없거나 0인 경우
#       동시에, in_condition이 이미 M인 경우
#       뽑을 수 없음.
#   뽑을 수 없는 경우 반복 종료

# out_condition 도 만족하는지 확인 후
# 만족하면 j - i + 1로 길이 계산 후 정답 갱신
def push(idx):
    global in_condition, out_condition
    num = arr[idx]
    if in_count[num] == 0:
        in_condition += 1
    in_count[num] += 1

    out_count[num] -= 1
    if out_count[num] == 0:
        out_condition -= 1

def pop(idx):
    global in_condition, out_condition
    num = arr[idx]
    in_count[num] -= 1
    if in_count[num] == 0:
        in_condition -= 1
    
    if out_count[num] == 0:
        out_condition += 1
    out_count[num] += 1

out_count = [0] * (m + 1)
in_count = [0] * (m + 1)
for ele in arr[1:]:
    out_count[ele] += 1
out_condition = m
in_condition = 0
j = 0
answer = float('inf')
for i in range(1, n + 1):
    while j + 1 <= n and in_condition < m:
        push(j + 1)
        j += 1

    if in_condition < m:
        break
    
    if out_condition == m:
        answer = min(answer, j - i + 1)
    
    pop(i)

print(-1 if answer == float('inf') else answer)