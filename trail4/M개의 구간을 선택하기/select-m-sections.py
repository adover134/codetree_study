N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# Please write your code here.
# 상태를 어떻게 정의해야?
# 현재 숫자에서 구간이 늘어나는 경우
# 현재 숫자에서 새 구간이 시작하는 경우?

# 구간은 최대 (M*2+1) 개 만든다고 가정한다.
# 짝수 번째 구간 (j%2 == 1)에 넣을 때에는 합이 증가

t = M*2 + 1
dp = [[-500001 for _ in range(t)] for _ in range(N+1)]
# dp[1][0] = 0
dp[1][1] = numbers[0]
for i in range(2, N+1):
    dp[i][1] = max(dp[i-1][1], 0) + numbers[i-1]
    for j in range(2, min(t, i+1)):
        if (j % 2) == 1:
            # 1. 현재 구간을 새로 시작하는 경우
            # 2. 현재 구간에 더하는 경우
            t1 = dp[i-1][j-1]+numbers[i-1]
            t2 = dp[i-1][j]+numbers[i-1]
            dp[i][j] = max(t1, t2)
        else:
            # 1. 현재 구간을 새로 시작하는 경우
            # 2. 현재 구간에 더하는 경우
            t1 = dp[i-1][j-1]
            t2 = dp[i-1][j]
            dp[i][j] = max(t1, t2)
print(max(dp[-1][-1], dp[-1][-2]))