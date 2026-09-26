n, m, t = map(int, input().split())

r = []
c = []
d = []
w = []

for _ in range(m):
    ri, ci, di, wi = input().split()
    r.append(int(ri))
    c.append(int(ci))
    d.append(di)
    w.append(int(wi))

# Please write your code here.
Map = [[[0, -1, ''] for _ in range(n + 1)] for _ in range(n + 1)]
marbles = [[i, R, C, D, W] for i, (R, C, D, W) in enumerate(zip(r, c, d, w))]

for _ in range(t):
    next_marbles = []
    for I, R, C, D, W in marbles:
        match D:
            case 'U':
                if R == 1:
                    ar = R
                    D = 'D'
                else:
                    ar = R - 1
                Map[ar][C][0] += W
                if Map[ar][C][1] < I:
                    Map[ar][C][1] = I
                    Map[ar][C][2] = D
            case 'D':
                if R == n:
                    ar = R
                    D = 'U'
                else:
                    ar = R + 1
                Map[ar][C][0] += W
                if Map[ar][C][1] < I:
                    Map[ar][C][1] = I
                    Map[ar][C][2] = D
            case 'L':
                if C == 1:
                    ac = C
                    D = 'R'
                else:
                    ac = C - 1
                Map[R][ac][0] += W
                if Map[R][ac][1] < I:
                    Map[R][ac][1] = I
                    Map[R][ac][2] = D
            case 'R':
                if C == n:
                    ac = C
                    D = 'L'
                else:
                    ac = C + 1
                Map[R][ac][0] += W
                if Map[R][ac][1] < I:
                    Map[R][ac][1] = I
                    Map[R][ac][2] = D
    for R in range(1, n + 1):
        for C in range(1, n + 1):
            if Map[R][C][1] > -1:
                next_marbles.append([Map[R][C][1], R, C, Map[R][C][2], Map[R][C][0]])
                Map[R][C] = [0, -1, '']
    marbles = next_marbles
print(len(next_marbles), max(m[-1] for m in marbles))
