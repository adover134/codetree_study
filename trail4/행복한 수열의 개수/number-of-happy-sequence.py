n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
a = 0
for g in grid:
    for j in range(n-m+1):
        if len(set(g[j:j+m])) == 1:
            a += 1
            break
for g in zip(*grid):
    for j in range(n-m+1):
        if len(set(g[j:j+m])) == 1:
            a += 1
            break
print(a)