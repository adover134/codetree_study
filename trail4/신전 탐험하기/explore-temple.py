n = int(input())
l, m, r = [], [], []
for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)

# Please write your code here.
dp = [[0 for _ in range(3)] for _ in range(n)]
items = list(zip(l,m,r))
for j in range(3):
    dp[0][j] = items[0][j]
for i in range(1, n):
    for j in range(3):
        dp[i][j] = items[i][j]+max(dp[i-1][d] for d in range(3) if d != j)
print(max(dp[-1]))