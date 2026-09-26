n, m, t, k = map(int, input().split())

r, c, d, v = [], [], [], []
for _ in range(m):
    ri, ci, di, vi = input().split()
    r.append(int(ri))
    c.append(int(ci))
    d.append(di)
    v.append(int(vi))

# Please write your code here.
marbles = sorted([[i, r[i], c[i], d[i], v[i] % (2 * (n - 1))] for i in range(m)], key = lambda x: [-x[4], -x[0]])
for i in range(m):
    marbles[i] = tuple(marbles[i][1:])
for T in range(t):
    temp = []
    found = {}
    for r, c, d, v in marbles:
        match d:
            case 'U':
                tv = v
                if tv > (r - 1):
                    tv -= (r - 1)
                    r = 1
                    d = 'D'
                    if tv >= (n - 1):
                        r = n
                        tv -= (n - 1)
                        d = 'U'
                    else:
                        r += tv
                        tv = 0
                r -= tv
            case 'D':
                tv = v
                if tv > (n - r):
                    tv -= (n - r)
                    r = n
                    d = 'U'
                    if tv >= (n - 1):
                        r = 1
                        tv -= (n - 1)
                        d = 'D'
                    else:
                        r -= tv
                        tv = 0
                r += tv
            case 'L':
                tv = v
                if tv > (c - 1):
                    tv -= (c - 1)
                    c = 1
                    d = 'R'
                    if tv >= (n - 1):
                        c = n
                        tv -= (n - 1)
                        d = 'L'
                    else:
                        c += tv
                        tv = 0
                c -= tv
            case 'R':
                tv = v
                if tv > (n - c):
                    tv -= (n - c)
                    c = n
                    d = 'L'
                    if tv >= (n - 1):
                        c = 1
                        tv -= (n - 1)
                        d = 'R'
                    else:
                        c -= tv
                        tv = 0
                c += tv
        # 해당 위치의 구슬이 이미 있다면
        # 기존 구슬은 지우고
        # 새 구슬만 추가
        if (r, c) in found:
            if found[(r, c)] < k:
                temp.append((r, c, d, v))
                found[(r, c)] += 1
        else:
            temp.append((r, c, d, v))
            found[(r, c)] = 1
    marbles = temp
print(len(marbles))