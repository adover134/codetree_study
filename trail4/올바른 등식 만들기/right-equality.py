N, M = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
# N 개의 정수를 모두 써서
# 최대 -20부터 20까지의 합을 만들 수 있으며
# M이 나오는 개수를 구하라.
# 그러면 1~N까지
# 합이 j는 그 시점에서의 합이 되도록
# 각 칸은 그 합이 되는 것의 개수이다.
offset=20
dp=[[0 for _ in range(41)] for _ in range(N+1)]
dp[0][20]=1
for i in range(1,N+1):
    for j in range(41):
        t = j-nums[i-1]
        if t >= 0 and t <= 40:
            dp[i][j] += dp[i-1][t]
        t = j+nums[i-1]
        if  t>= 0 and t <= 40:
            dp[i][j] += dp[i-1][t]
print(dp[-1][M+20])