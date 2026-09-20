n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
maxi = 0
for i in range(n):
    for h in range(n-i,0,-1):
        area = zip(*[g for g in grid[i:i+h]])
        s = 0
        for c in area:
            f = False
            for num in c:
                if num <= 0:
                    f = True
                    break
            if not f:
                s += h
                maxi = max(s, maxi)
            else:
                s = 0
if maxi > 0:
    print(maxi)
else:
    print(-1)