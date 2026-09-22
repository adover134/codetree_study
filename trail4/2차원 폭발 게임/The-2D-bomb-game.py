n, m, k = map(int, input().split())
numbers_2d = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

def remove_cells():
    global numbers_2d
    t = zip(*numbers_2d)
    numbers_2d = []
    for c, g in enumerate(t):
        tt = []
        while g:
            f = True
            ranges = []
            cur = 0
            cnt = 1
            for r in range(1, len(g)):
                if g[cur] == g[r]:
                    cnt += 1
                else:
                    ranges.append((cur, cnt))
                    cur = r
                    cnt = 1
            ranges.append((cur, cnt))
            for cur, cnt in reversed(ranges):
                if cnt >= m:
                    f = False
                    g = g[:cur]+g[cur+cnt:]
            if f:
                break
        if g:
            g = list(g)[::-1] + [0] * (n - len(g))
            numbers_2d.append(g)
        

def fall_down():
    global numbers_2d
    for r in range(len(numbers_2d) - 1):
        for c in range(n):
            if numbers_2d[r+1][c] == 0:
                for rr in range(r, -1, -1):
                    numbers_2d[rr+1][c] = numbers_2d[rr][c]
                    numbers_2d[rr][c] = 0

for K in range(k):
    remove_cells()
    fall_down()
remove_cells()
cnt = 0
for g in numbers_2d:
    cnt += sum(n > 0 for n in g)
print(cnt)