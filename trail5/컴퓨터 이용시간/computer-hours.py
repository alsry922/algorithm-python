import heapq
n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
# p = [interval[0] for interval in intervals]
# q = [interval[1] for interval in intervals]

# Please write your code here.
available_computers = [i for i in range(1, n + 1)]
heapq.heapify(available_computers)
events = []
for index, (p, q) in enumerate(intervals):
    events.append((p, +1, index))
    events.append((q, -1, index))
events.sort()
used = [0] * n
for x, v, index in events:
    if v == 1:
        comp_num = heapq.heappop(available_computers)
        used[index] = comp_num
    else:
        comp_num = used[index]
        heapq.heappush(available_computers, comp_num)

print(*used)
