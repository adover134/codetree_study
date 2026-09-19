n = int(input())
jobs = sorted(tuple(map(int, input().split())) for _ in range(n))
s = [job[0] for job in jobs]
e = [job[1] for job in jobs]
p = [job[2] for job in jobs]

# Please write your code here.
dp = [0 for _ in range(n)]
# dp[i]는 i번째 알바를 할 때 얻을 수 있는 최댓값이다.
for i in range(n):
    dp[i] = p[i]
    for j in range(i):
        if s[i] > e[j]:
            dp[i] = max(dp[i], dp[j] + p[i])
print(max(dp))