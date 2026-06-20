from collections import defaultdict
n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
# 같은 값이 k개 이하가 되도록 배열에서 원소를 연속으로 뽑았을 때 그 길이가 최대가 되도록 하라.
# 각 값이 현재 몇 개가 뽑혔는지 dict로 관리
# i, j를 왼쪽, 오른쪽 포인터로 두고 투 포인터 탐색
# while 을 반복하며 j + 1이 범위 안에 있고, j + 1 위치의 수가 현재 k개 미만이면 j를 확장 가능
#   안되면 j 확장을 멈추고 현재까지의 연속 부분 수열의 길이를 구해서 답을 갱신
#   i를 확장하면서 i 위치의 수의 count를 하나 줄임.

count = defaultdict(int)
j = 0
answer = 1
for i in range(1, n + 1):
    while j + 1 <= n and count[arr[j + 1]] < k:
        count[arr[j + 1]] += 1
        j += 1

    answer = max(answer, j - i + 1) 

    count[arr[i]] -= 1

print(answer)