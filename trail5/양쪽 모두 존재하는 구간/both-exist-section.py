from collections import defaultdict
n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
outside_cnt = defaultdict(int)
for i in range(1, n + 1):
    num = arr[i]
    outside_cnt[num] += 1
inside_cnt = defaultdict(int)
inside_full = 0
outside_full = len(set(arr)) - 1
# 특정 구간에 1이상 M이하의 수가 적어도 하나씩 존재할 때 가장 짧은 구간의 길이를 출력
# 구간 -> 슬라이딩 윈도우
# 고정된 구간을 이동시키며 구하지 않음 -> 가변 윈도우
# 슬라이딩 윈도우 문제니까 투 포인터 사용 가능 한가?
# i, j 투 포인터를 잡음
#   [i, j] 구간에서 i가 증가하게 되면 1 ~ M 수 중 하나가 줄어들게 됨.
#   i를 증가시킨 경우에도 조건이 만족한다면, j를 그대로 두거나
#   만족하지 않는다면, j를 증가시켜서 1 ~ M 사이의 원소 하나를 찾아야 함.
#   i가 증가할 때 j도 같은 방향으로 움직여야함 -> 단조성 발견, 투 포인터 사용 가능
# 모든 원소가 몇 번 등장했는지 hashmap(outside)으로 관리
# 특정 구간에서 어떤 원소가 몇 번 등장했는지 hashmap(inside)으로 관리
# inside에 원소 추가할 때마다 all에서는 해당 원소의 갯수를 줄임.
# inside에 원소 제거할 때마다 all에서는 해당 원소의 갯수를 올림.
# inside에 1 ~ M 이하의 수가 적어도 하나씩 존재할 때까지 반복.
#   조건을 만족하게 되면 while문 탈출
#   all에도 1 ~ M 이하의 수가 적어도 하나씩 있는지 확인
#       있다면 j - i + 1을 계산하여 답 갱신
#       없다면 답 갱신 X
#       i값 증가
#       다시 조건을 만족시키는 경우가 나올 때까지 j를 확장

# inside_cnt에 1 ~ M 사이의 숫자가 적어도 하나씩 있는지 확인
def increase_inside_full():
    global inside_full
    inside_full += 1

j = 0
answer = float('inf')
for i in range(1, n + 1):
    # inside 조건을 만족할 때까지 반복
    while j + 1 <= n and inside_full < m:
        num = arr[j + 1]
        # inside에 없던 수가 추가되면, inside_full 증가
        if inside_cnt[num] == 0:
            inside_full += 1
        inside_cnt[num] += 1
        # inside에 num을 추가하니까 outside에 num을 하나 제거
        # outside에 num의 갯수가 0이 되면 outside_full 감소
        if outside_cnt[num] > 0:
            outside_cnt[num] -= 1
            if outside_cnt[num] == 0:
                outside_full -= 1
            
        j += 1
    
    if inside_full < m:
        break
    
    # ouside 조건도 만족하면 
    if outside_full >= m:
        answer = min(answer, j - i + 1)        
    
    # inside에서 arr[i] 제거
    # inside에 해당 수가 0이되면 inside_full 감소
    if inside_cnt[arr[i]] > 0:
        inside_cnt[arr[i]] -= 1
        if inside_cnt[arr[i]] == 0:
            inside_full -= 1
    # outside에 arr[i] 추가
    # outside에 arr[i]가 없었으면 outside_full 증가
    if outside_cnt[arr[i]] == 0:
        outside_full += 1
    outside_cnt[arr[i]] += 1

print(-1 if answer == float('inf') else answer)
    