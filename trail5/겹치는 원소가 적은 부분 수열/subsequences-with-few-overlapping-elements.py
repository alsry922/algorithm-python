from collections import defaultdict
n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
# 연속 부분 수열
#   슬라이딩 윈도우
# 가장 긴 연속 부분 수열 찾기
#   가변 윈도우
# 투 포인터 사용 가능한가?
#   p[i] = [i, n - 1] 범위의 같은 원소가 k개 이하로 들어있는 가장 긴 부분 연속 수열 길이라고 정의한다면
#   두 포인터 i, j를 잡았을 때, i가 증가할 때 j가 뒤로 돌아갈 필요 없음.
#   i와 j가 각각 한 방향으로 움직이므로 단조성 확인
# 한 원소가 몇 개가 들어있는지 hashmap으로 관리
#   뽑아야 할 원소가 k 개 미만일 때까지만 반복하며 hashmap에 추가

subsequence = defaultdict(int)
p = [0] * (n + 1)
j = 0
for i in range(1, n + 1):
    while j + 1 <= n and subsequence[arr[j + 1]] < k:
        subsequence[arr[j + 1]] += 1
        j += 1
    p[i] = j - i + 1
    subsequence[arr[i]] -= 1

print(max(p))
