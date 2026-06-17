n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]

# Please write your code here.
# A1 ~ An을 각 그룹 내의 수들끼리의 차가 K를 넘지 않도록 두 개의 그룹으로 나눴을 때, 그룹의 최대 크기 출력
# 그룹의 최댓값과 최솟값의 차가 K를 넘지 않아야 함.
# 하나의 원소는 하나의 그룹에만 속할 수 있음.
# 정렬된 배열에서 원소가 겹치지 않도록 선택해 두 개의 그룹으로 나눌 때,
# 특정 구간 p를 기준으로 L1 ~ R1, L2 ~ R2 (R1 < L2) 이거나 (R2 < L1) 으로 나뉨.
# L[i] = [0, i]까지 고려했을 때 조건을 만족하는 그룹의 최대 크기
# R[i] = [i, n -1]까지 고려했을 때 조건을 만족하는 그룹의 최대 크기
# LR 값을 구할 때 투 포인터를 사용하여 계산할 수 있음(i, j를 투 포인터로 잡았을 때 i, j가 한 방향으로만 이동함.)
#   i가 증가하면 두 수의 차가 줄어드니까 당연히 더 큰 크기의 그룹을 구하기 위해서는 j도 증가해야 함.
#   반대 방향으로는 i가 감소할 시 j도 감소
# LR 테크닉을 사용하여 미리 최대 크기를 정해두고, 특정 구간 p에 속하는 위치를 가지고 전부 다 계산하여 답을 갱신
# answer = max(answer, L[i] + R[i + 1])
nums = sorted(nums)
j = 0
answer = 0
L = [0] * (n)
R = [0] * (n)
# L[0] = 1
# R[n - 1] = 1
for i in range(n):
    # 다음 위치가 범위 안에 있고, 다음 수와 현재 i번째 수의 차가 K 이하인 경우 반복 가능
    while j < n and nums[i] - nums[j] > k:
        j += 1
    if i == 0:
        L[i] = abs(i - j) + 1
    else:
        L[i] = max(L[i - 1], abs(i - j) + 1)

j = n - 1
for i in range(n - 1, -1, -1):
    while j >= 0 and nums[j] - nums[i] > k:
        j -= 1
    if i == n - 1:
        R[i] = abs(i - j) + 1
    else:
        R[i] = max(R[i + 1], abs(i - j) + 1)

answer = max(answer, L[n - 1])
for i in range(n - 1):
    answer = max(answer, L[i] + R[i + 1])

print(answer)
    