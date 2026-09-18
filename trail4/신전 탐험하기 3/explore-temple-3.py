n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
for i in range(1, n):
    for j in range(m):
        maxi = 0
        for k in range(m):
            if k == j:
                continue
            if maxi < a[i-1][k]:
                maxi = a[i-1][k]
        a[i][j] += maxi
print(max(a[-1]))        
