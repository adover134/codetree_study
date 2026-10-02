n, m = map(int, input().split())

A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

# Please write your code here.
ans = 0
for i in range(m - 2):
    for j in range(i + 1, m - 1):
        for k in range(j + 1, m):
            As = set([A[l][i]+A[l][j]+A[l][k] for l in range(n)])
            Bs = set([B[l][i]+B[l][j]+B[l][k] for l in range(n)])
            if len(As.intersection(Bs)) == 0:
                ans += 1
print(ans)