n = int(input())
grid = [list(input()) for _ in range(n)]

# Please write your code here.
non_num = {'.','S','E'}
pos = [0]*10
coins = set()
s = [0,0]
e = [0,0]
for r in range(n):
    for c in range(n):
        if grid[r][c] not in non_num:
            p = int(grid[r][c])
            pos[p] = (r,c)
            coins.add(p)
        elif grid[r][c] == 'S':
            s = [r, c]
        elif grid[r][c] == 'E':
            e = [r, c]
coins = sorted(coins)
m = len(coins)

if m > 2:

    mini = n*2*4+1

    for i in range(m-2):
        ti = coins[i]
        d = abs(pos[ti][0]-s[0])+abs(pos[ti][1]-s[1])
        for j in range(i+1,m-1):
            tj = coins[j]
            d += abs(pos[tj][0]-pos[ti][0])+abs(pos[tj][1]-pos[ti][1])
            for k in range(j+1,m):
                tk = coins[k]
                d += abs(pos[tk][0]-pos[tj][0])+abs(pos[tk][1]-pos[tj][1])
                d += abs(e[0]-pos[tk][0])+abs(e[1]-pos[tk][1])
                if mini > d:
                    mini = d
                d -= abs(pos[tk][0]-pos[tj][0])+abs(pos[tk][1]-pos[tj][1])
                d -= abs(e[0]-pos[tk][0])+abs(e[1]-pos[tk][1])
            d -= abs(pos[tj][0]-pos[ti][0])+abs(pos[tj][1]-pos[ti][1])
    print(mini)

else:
    print(-1)