from sortedcontainers import SortedSet

# 변수 선언 및 입력:
n, q = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
queries = [
    tuple(map(int, input().split()))
    for _ in range(q)
]

mapper = {}

# 주어진 x좌표값들을 전부 treeset에 넣어줍니다.
nums = SortedSet(arr)

# 예외를 처리하기 위해 최댓값보다 큰 값을 treeset에 넣어줍니다.
nums.add((10 ** 9) + 1)

# treeset에서 정점을 작은 번호부터 뽑으면서
# 각 정점별로 1번부터 순서대로 매칭하여
# 그 결과를 hashmap에 넣어줍니다.
cnt = 1
for num in nums:
    mapper[num] = cnt
    cnt += 1

# 질의에 대해
# 각 [a, b]에 해당하는 번호를
# mapper를 통해 구해
# 두 번호 사이의 점의 수를 출력합니다.
for a, b in queries:
    new_a = mapper[nums[nums.bisect_left(a)]]
    new_b = mapper[nums[nums.bisect_right(b)]]

    print(new_b - new_a)
