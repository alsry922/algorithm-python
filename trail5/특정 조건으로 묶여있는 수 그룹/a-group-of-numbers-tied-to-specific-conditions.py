n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]

# Please write your code here.
nums.sort()
left_best = [0] * (n)
right_best = [0] * (n)
# 그룹 내 최솟값과 최댓값의 차가 K를 넘지 않도록 그룹을 구성한다.
# nums를 정렬하고 two pointer를 사용한다.
# 정렬한 상태에서 i, j 투 포인터를 사용해서 그룹에 수를 추가하면,
# 자연스럽게 i 위치의 수가 그룹의 최솟값, j 위치의 수가 그룹의 최댓값이 된다.
# nums[j] - nums[i](정렬된 상태이기 때문에 j위치 수가 i위치 수 보다 크다는 것이 확실함)값이 K 이하인 경우,
# j위치의 수를 그룹에 추가하고 j를 증가시키는 과정을 반복한다.
# nums[j] - nums[i] 의 값이 K 초과인 경우 반복문을 탈출한다.
# left_best[p] = [0, p] 구간 안에서 만들 수 있는 최대 그룹 크기
# right_best[p] = [p, n - 1] 구간 안에서 만들 수 있는 최대 그룹 크기

i = 0 # 왼쪽 끝
for j in range(n): # j는 오른쪽 끝
    while nums[j] - nums[i] > k:
        i += 1
    left_best[j] = max(left_best[j - 1] if j > 0 else 0, j - i + 1)

# print(left_best)
i = n - 1 # 오른쪽 끝
for j in range(n - 1, -1, -1): # j는 왼쪽 끝
    while nums[i] - nums[j] > k:
        i -= 1
    right_best[j] = max(right_best[j + 1] if j < n - 1 else 0, i - j + 1)

# print(right_best)

answer = 0
for i in range(n - 1):
    answer = max(answer, left_best[i] + right_best[i + 1])

print(answer)