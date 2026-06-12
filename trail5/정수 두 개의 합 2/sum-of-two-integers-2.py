n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
# 두 개의 원소의 합이 K 이하가 되어야 함
#   two sum 문제
#   A + B <= k 를 만족시켜야 함.
#   A를 고를 때마다 B <= k - A 를 만족하는 B가 몇 개나 있는지 확인할 수 있어야 함.
#   배열을 정렬하고 A를 선택한 후에 bisect.right(k - A)의 인덱스(B의 인덱스)를 구하고
#   A 인덱스와 B 인덱스의 차를 구하면 경우의 수가 됨.
#   모든 경우의 수를 더해서 출력
# 두 개를 고르는 거니까 two pointer로 가능한가?
#   배열을 정렬하고, i, j 투 포인터를 설정.
#   i가 증가함에 따라 j도 증가하도록 설정할 수 없음.
#   i가 증가하면, arr[i] + arr[j] <= k 를 만족하는 최대 j는 감소해야 함
#   j가 뒤로 가야하므로 가은 방향 불가.
#   i는 증가, j는 감소하는 방향으로 단조성을 설정
#   arr[i] + arr[j] > k 라면 j를 줄여 합을 줄이고, arr[i] + arr[j] <= k 라면 i를 늘려 합을 늘리면 됨.
#   정답 조건에 맞는 경우가 되면 마찬가지로 두 인덱스의 차를 통해 경우의 수를 구하고,
#   모든 경우의 수를 구하여 출력
arr.sort()
j = n - 1
answer = 0
for i in range(n):
    while i < j and arr[i] + arr[j] > k:
        j -= 1
    
    # 계속 살펴봤는데 k 이하인 조건을 만족하지 못한 경우
    if i == j:
        break

    answer += (j - i)

print(answer)
    