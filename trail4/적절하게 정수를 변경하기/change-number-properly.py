N, M = map(int, input().split())
a = [0] + list(map(int, input().split()))

# Please write your code here.
# 인접한 두 값이 다른 횟수가 n회 이하여야 된다.
# 주어진 수열을 먼저 보고
# 그 수열을 기준으로, '비슷한 수열'임을 유지하면서

# dp[i][j][k]는 i번째 수에서 j를 고른 경우, 비슷 값이 k일 때의 유사도이다.
# 여기서 '비슷 값'은 인접 두 수가 다른 경우 1 늘어난다고 가정하자.
# j의 범위는 4까지
# k의 범위는 M까지이다.
dp = [[[0 for _ in range(M+1)] for _ in range(4)] for _ in range(N+1)]
if M > 0:
    for j in range(4):
        if j == (a[1]-1):
            dp[1][j][0] = 1
        else:
            dp[1][j][1] = 0
else:
    for j in range(4):
        if j == (a[1]-1):
            dp[1][j][0] = 1

for i in range(2, N+1):
    for j in range(4):
        # k가 0이라면
        # 직전과 동일한 j를 골랐다는 뜻이다.
        dp[i][j][0] = dp[i-1][j][0]
        dp[i][j][0] += (a[i]==(j+1))
        for k in range(1, M+1):
            t = 0
            for m in range(4):
                if m == j:
                    t = max(dp[i-1][m][k], t)
                else:
                    t = max(dp[i-1][m][k-1], t)
            dp[i][j][k] = t
            dp[i][j][k] += (a[i]==(j+1))

print(max(max(d) for d in dp[-1]))