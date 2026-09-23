n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# k번 위치부터 m개의 블록이 떨어진다.
mini = n - 1
for i in range(k-1, k - 1 + m):
    for j in range(n - 1):
        if grid[j + 1][i] == 1:
            mini = min(mini, j)
            break
for i in range(k - 1, k - 1 + m):
    grid[mini][i] = 1
for i in range(n):
    for j in range(n):
        print(grid[i][j], end = ' ')
    print()