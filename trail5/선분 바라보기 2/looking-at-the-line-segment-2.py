from sortedcontainers import SortedSet
n = int(input())
segments = []
for _ in range(n):
    yi, x1i, x2i = map(int, input().split())
    segments.append((yi, x1i, x2i))
    

# Please write your code here.
# y값이 작은 순으로 정렬
segments.sort()
covered = SortedSet()
cnt = 0
for segment in segments:
    _, x1, x2 = segment
    # 히나도 없으면 제일 앞에 있는 선분이므로 보임.
    if not covered:
        covered.add((x1, x2))
        cnt += 1
        continue
    
    # 앞에 있는 선분과 겹치는 선분이 있는지 확인
    idx = covered.bisect_right((x1, x2)) - 1
    if idx < 0:
        idx += 1
    
    # 현재 선분이 앞에 있는 선분에 완전히 겹쳐진다면 넘어가기.
    cx1, cx2 = covered[idx]
    if cx1 <= x1 and x2 <= cx2:
        continue
    # 만약 완전히 겹치지 않는다면 보이는 거임
    cnt += 1
    to_remove = []
    # 현재 선분과 겹치는 선분을 파악하기
    mx1, mx2 = x1, x2
    for i in range(idx, len(covered)):
        cx1, cx2 = covered[i]
        if cx1 > x2:
            break
        if cx1 < x1 < cx2 or cx1 < x2 < cx2 or x1 < cx1 and cx2 < x2:
            mx1 = min(mx1, cx1)
            mx2 = max(mx2, cx2)
            to_remove.append(covered[i])
    # 겹치는 선분이 없으면 covered에 추가
    if not to_remove:
        covered.add((x1, x2))
    else:
        # 겹치는 선분을 covered에서 merge해서 하나의 선분으로 처리하기
        for ele in to_remove:
            covered.remove(ele)
        covered.add((mx1, mx2))

print(cnt)