s = input()
t = input()

# Please write your code here.
# i, j는
# s[i-1]과 t[j-1]이 같을 경우 1만 증가
# 아니라면 dp[i-1][j-1]+2, dp[i-1][j]+1, dp[i][j-1]+1 중 하나
ls, lt = len(s), len(t)
dp = [[0 for _ in range(lt+1)] for _ in range(ls+1)]

for i in range(ls+1):
    dp[i][0] = i
for j in range(lt+1):
    dp[0][j] = j

for i in range(1, ls+1):
    for j in range(1, lt+1):
        dp[i][j] = min([dp[i-1][j-1]+2,dp[i][j-1]+1,dp[i-1][j]+1])
        if s[i-1] == t[j-1]:
            dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)

print(dp[-1][-1])