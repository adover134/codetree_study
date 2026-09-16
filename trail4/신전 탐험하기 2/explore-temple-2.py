n = int(input())
l, m, r = [], [], []

for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)

# Please write your code here.
items = list(zip(l, m, r))
def find_max(s):
    dp = [0 for j in range(3)]
    dp[s] = items[0][s]
    for i in range(1, (n-1)):
        t = [0 for j in range(3)]
        for j in range(3):
            t[j] = items[i][j]+max(dp[d] for d in range(3) if d != j)
        dp = t
    a = 0
    for j in range(3):
        if j == s:
            continue
        t = max(items[-1][j]+dp[d] for d in range(3) if d != j)
        a = max(a, t)
    return a

res = [find_max(j) for j in range(3)]
print(max(res))
