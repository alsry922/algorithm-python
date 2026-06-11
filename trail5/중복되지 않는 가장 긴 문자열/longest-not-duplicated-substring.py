word = [None] + list(input())

# Please write your code here.
# 투 포인터 i, j를 증가시키며 원소를 살핀다.
# j위치 원소가 j + 1위치 원소보다 + 1 큰 문자면 j를 증가시키는 작업을 반복한다.
# 아니라면 j - i를 계산해 현재 정답과 비교하여 갱신한다.

j = 0
answer = 1
n = len(word)
substr = set()
for i in range(1, n):
    if i > j:
        j += 1
        substr.add(word[j])

    while j + 1 < n and word[j + 1] not in substr:
        substr.add(word[j + 1])
        j += 1
    
    answer = max(answer, j - i + 1)
    substr.remove(word[i])

print(answer)
