n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
m = 0
for i in range(n-2):
    for j in range(n-2):
        m = max(m, sum(sum(g[j:j+3]) for g in grid[i:i+3]))
print(m)