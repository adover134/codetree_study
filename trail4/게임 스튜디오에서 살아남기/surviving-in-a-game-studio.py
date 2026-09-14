n = int(input())

# Please write your code here.
# T를 받을 수 있는 횟수는 최대 3번
# B를 받을 수 있는 횟수는 연속으로는 최대 3번
# dp[i][j][k]로 3차원으로 만들자.
# i는 일자
# j는 T를 받은 횟수
# k는 B를 직전 연속 받은 횟수
# 만약 오늘 G라면, 이전의 B streak이 깨진다.
# 만약 T라도 B streak은 깨진다.
dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(n + 1)]
dp[0][0][0] = 1
for i in range(1, n+1):
    # T 횟수가 0인 경우, B가 0인 경우는 G를 통한 초기화만 있다.
    dp[i][0][0] = sum(dp[i-1][0])%1000000007
    # B 횟수 증가는 이전 단계에서의 1 증가만 있다.
    for k in range(1, 3):
        dp[i][0][k] = dp[i-1][0][k-1]
    for j in range(1, 3):
        # dp[i-1][j]는 T 받은 횟수를 유지하면서, G로 B 스택 초기화
        # dp[i-1][j-1]은 T 받은 횟수가 증가하는 경우
        dp[i][j][0] = (sum(dp[i-1][j])+sum(dp[i-1][j-1]))%1000000007
        # B가 증가하기 위해서는 이전의 B보다 1 늘어나야만 한다.
        # 즉, T 횟수를 증가하는 방향은 불가능하다.
        for k in range(1, 3):
            dp[i][j][k] = dp[i-1][j][k-1]
print(sum(sum(d) % 1000000007 for d in dp[-1]) % 1000000007)