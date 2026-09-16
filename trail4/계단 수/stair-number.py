n = int(input())

# Please write your code here.
# dp[i][j]는 i번째 수가 j인 경우의 수이다.
MOD = 1000000007
dp = [[0 for _ in range(10)] for _ in range(n)]
for j in range(1, 10):
    dp[0][j] += 1
for i in range(1, n):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1, 9):
        dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1])%MOD
print(sum(dp[-1])%MOD)