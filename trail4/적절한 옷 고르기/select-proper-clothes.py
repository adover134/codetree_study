N, M = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(N)]
s = [x[0] for x in clothes]
e = [x[1] for x in clothes]
v = [x[2] for x in clothes]

# Please write your code here.
# 만족도는
# 인접 날짜의 화려함과의 차이의 절댓값이다.

# s[i]는 i 번째 옷을 입기 시작할 수 있는 날
# e[i]는 i 번째 옷을 입을 수 있는 마지막 날
# v[i]는 i 번째 옷의 화려함

# 매일 하나를 골라야 한다.
# dp[i][j]는 i번째 날에 j번째 옷을 입는 경우이다.

dp = [[0 for _ in range(N)] for _ in range(M)]
for j in range(N):
    if s[j] > 1:
        dp[0][j] = -float('inf')

for i in range(1, M):
    for j in range(N):
        if (s[j]-1) <= i and (e[j]-1) >= i:
            dp[i][j] = max([abs(v[j]-v[k])+dp[i-1][k] for k in range(N)])
        else:
            dp[i][j] = -float('inf')

print(max(dp[-1]))