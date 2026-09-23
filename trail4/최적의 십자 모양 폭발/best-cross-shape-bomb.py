n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from copy import deepcopy
def falldown(A):
    t = []
    for c in zip(*A):
        tc = []
        for num in c:
            if num == 0:
                continue
            tc.append(num)
        tc = tc[::-1]
        for _ in range(len(tc), n):
            tc.append(0)
        t.append(tc)
    return t

def explode(r, c):
    global grid
    t = deepcopy(grid)
    dr, dc = [0, 0, -1, 1], [1, -1, 0, 0]
    t[r][c] = 0
    for i in range(1, grid[r][c]):
        for d in range(4):
            ar, ac = r + dr[d] * i, c + dc[d] * i
            if ar < 0 or ar >= n or ac < 0 or ac >= n:
                continue
            t[ar][ac] = 0

    t = falldown(t)
    ans = 0
    for r in t:
        for i in range(1, n):
            if r[i] == r[i-1] and r[i] > 0:
                ans += 1
    for i in range(n):
        for j in range(1, n):
            if t[j-1][i] == t[j][i] and t[j][i] > 0:
                ans += 1
    return ans
maxi = 0
for i in range(n):
    for j in range(n):
        maxi = max(explode(i, j), maxi)
print(maxi)