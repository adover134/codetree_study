n = int(input())
s = []
b = []
for _ in range(n):
    si, bi = map(int, input().split())
    s.append(si)
    b.append(bi)

# Please write your code here.
# dp[i][j][k]는 축구부는 j명, 야구부를 k명 골랐을 경우이다.
# 둘 다 안 고르는 경우도 있으며
# 둘 다 최대인 경우만 골라야 한다.
dp = [[[0 for _ in range(10)] for _ in range(12)] for _ in range(n+1)]
dp[1][0][1] = b[0]
dp[1][1][0] = s[0]
for i in range(2, n+1):
    for k in range(1, 10):
        if dp[i-1][0][k] == 0:
            dp[i][0][k] = dp[i-1][0][k-1]+b[i-1]
            break
        else:
            dp[i][0][k] = max(dp[i-1][0][k], dp[i-1][0][k-1]+b[i-1])
    for j in range(1, 12):
        if dp[i-1][j][0] == 0:
            dp[i][j][0] = dp[i-1][j-1][0]+s[i-1]
            break
        else:
            dp[i][j][0] = max(dp[i-1][j-1][0]+s[i-1], dp[i-1][j][0])
    for j in range(1, 12):
        for k in range(1, 10):
            if dp[i-1][j][k] == 0:
                dp[i][j][k] = max(dp[i-1][j-1][k]+s[i-1], dp[i-1][j][k-1]+b[i-1])
                break
            else:
                dp[i][j][k] = max([dp[i-1][j-1][k]+s[i-1], dp[i-1][j][k-1]+b[i-1], dp[i-1][j][k]])

print(dp[-1][11][9])