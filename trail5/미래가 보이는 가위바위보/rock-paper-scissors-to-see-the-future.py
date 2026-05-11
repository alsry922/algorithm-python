N = int(input())
B = [input() for _ in range(N)]

# Please write your code here.
def win_a(a, b):
    # H -> P -> S -> H
    if (a == 'H' and b == 'S') or \
        (a == 'P' and b == 'H') or \
        (a == 'S' and b == 'P'):
        return 1
    
    return 0

H = [0 for _ in range(N)]
S = [0 for _ in range(N)]
P = [0 for _ in range(N)]
# H 주먹, S 가위, P 보자기
LH = [0 for _ in range(N)]
RH = [0 for _ in range(N)]
LS = [0 for _ in range(N)]
RS = [0 for _ in range(N)]
LP = [0 for _ in range(N)]
RP = [0 for _ in range(N)]

for i in range(N):
    H = win_a('H', B[i])
    S = win_a('S', B[i])
    P = win_a('P', B[i])
    LH[i], LS[i], LP[i] = H, S, P
    RH[i], RS[i], RP[i] = H, S, P

for i in range(1, N):
    LH[i] += LH[i - 1]
    LS[i] += LS[i - 1]
    LP[i] += LP[i - 1]

for j in range(N - 2, -1, -1):
    RH[j] += RH[j + 1]
    RS[j] += RS[j + 1]
    RP[j] += RP[j + 1]

answer = 0
for i in range(1, N):
    answer = max(
        answer, 
        max(LH[i - 1], LS[i - 1], LP[i - 1]) + max(RH[i], RS[i], RP[i])
    )

print(answer)