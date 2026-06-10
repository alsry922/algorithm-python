n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
# 배열을 정렬
# i는 증가, j는 감소하면서 a[i] + a[j]를 계산해 M 값을 매번 갱신하며 정답을 찾는다.
# i는 증가, j는 감소하면서 찾는게 왜 가능한가?
# a[i] + a[j]가 0보다 큰 경우 j를 낮춘다.
#   정렬된 상태에서 a[j - 1] < a[j] 가 확실하기 때문에 합이 작아진다.
#   만약 i를 증가시키면 a[i + 1] + a[j] 는 이전보다 값이 더 커지기 때문에 원하는 답이 아니게 된다.
# a[i] + a[j]가 0보다 작은 경우 i를 증가시킨다.
#   앞선 이유와 마찬가지로 다음 차례에 계산한 값이 0과 가깝도록 하게 하기 위해서다.
# a[i] + a[j] == 0인 경우 바로 답을 찾은 경우이기 때문에 중단하고 답을 출력한다.

a.sort()
i = 0
j = n - 1
answer = float('inf')
# for i in range(n):
while i < j:
    if a[i] + a[j] > 0:
        answer = min(answer, abs(a[i] + a[j]))
        j -= 1
    elif a[i] + a[j] < 0:
        answer = min(answer, abs(a[i] + a[j]))
        i += 1
    elif a[i] + a[j] == 0:
        answer = 0
        break

print(answer)