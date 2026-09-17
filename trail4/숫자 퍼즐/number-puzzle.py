n, m, k = map(int, input().split())

# Please write your code here.
# digit DP 문제인가?
# 숫자 합은 반드시 M
# 2자리 숫자에 대해
# 합이 M이어야 하는 경우 가능한 개수를 구하자.
# 합 / 개수가 줄어든 경우를 구해야 하는데

dp = [[[-float('inf') for _ in range(m+1)] for _ in range(m+1)] for _ in range(n + 1)]

def fill_dp(coins, prev, remaining):
    if (prev * coins) > remaining:
        return 0
    global dp
    s = 0
    if coins == 0:
        if remaining == 0:
            dp[coins][prev][remaining] = 1
            return 1
        else:
            dp[coins][prev][remaining] = 0
            return 0
    if dp[coins][prev][remaining]==-float('inf'):
        dp[coins][prev][remaining] = 0
        if coins >= 1:
            dp[coins][prev][remaining] = fill_dp(coins-1, prev, remaining-prev)
        if (prev+1) <= remaining:
            dp[coins][prev][remaining] += fill_dp(coins, prev+1, remaining)
    return dp[coins][prev][remaining]
fill_dp(n, 1, m)

# dp[coins][value][remaining] = dp[coins-1][value][remaining-value] + dp[coins][value+1][remaining]

coins, value, remaining = n, 1, m
s = 0
while coins > 0:
    cnt = dp[coins-1][value][remaining-value]
    if s+ cnt < k:
        if cnt > 0:
            s += cnt
        value += 1
    else:
        coins -= 1
        remaining -= value
        print(value, end = ' ')