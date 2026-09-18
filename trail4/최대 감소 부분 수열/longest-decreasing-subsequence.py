n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
maxi = max(m)
dp = [-1 for _ in range(maxi+2)]
dp[maxi + 1] = 0
for i in range(n):
    a = m[i]
    for j in range(maxi+1, a, -1):
        if (dp[j]+1) > dp[a]:
            dp[a] = dp[j]+1
print(max(dp))