from collections import defaultdict

word, k = input().split()
k = int(k)
n = len(word)
# Please write your code here.
# 서로 다른 문자의 수가 K개를 넘지 않는 연속 부분 문자열을 을 구하고 최장 길이를 출력
# 연속한 구간을 탐색
#   -> 슬라이딩 윈도우
# 최장 길이를 구해야 함
#   -> 고정된 크기의 윈도우가 아닌 가변 크기 윈도우
#   -> 투 포인터 사용 고려
#  투 포인터 사용 가능 여부
#   i, j 포인터를 두고, j를 증가시키며 탐색한 문자를 map으로 저장하는 것을 반복
#   반복문을 빠져나와 j - i + 1로 길이를 구하고 나면 i 포인터를 증가시킴
#   이 때 j는 이전 j와 크거나 같음.
#   i와 j가 한 방향으로만 움직임. 단조성 확인. 따라서 투 포인터 사용 가능

j = 0
substr = defaultdict(int)
substr[word[0]] = 1
answer = 0
for i in range(n):
    while j + 1 < n:
        if word[j + 1] not in substr and len(substr) >= k:
            break
        substr[word[j + 1]] += 1
        j += 1
    
    answer = max(answer, j - i + 1)
    
    substr[word[i]] -= 1
    if substr[word[i]] == 0:
        substr.pop(word[i])

print(answer)

    