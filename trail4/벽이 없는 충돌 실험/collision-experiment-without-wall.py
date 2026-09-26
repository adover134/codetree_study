T = int(input())

for _ in range(T):
    N = int(input())
    x, y, w, d = [], [], [], []

    for i in range(N):
        xi, yi, wi, di = input().split()
        x.append(int(xi))
        y.append(int(yi))
        w.append(int(wi))
        d.append(di)

    # Please write your code here.
    # 왼쪽으로 가면서 x가 -1000인 경우는 무시
    # 오른쪽으로 가면서 x가 1000인 경우는 무시
    # 최대 횟수는 2000으로 두자.
    # 구슬들은 초 당 1씩 움직인다고 보고, 위치 값을 2배로 늘려서 해야 된다.
    # 초마다 구슬을 움직이고
    # 방향 기준으로 그 방향으로 더 가도 다른 구슬이 없으면 그 구슬은 없앤다.
    marbles = sorted([[i, x[i] * 2, y[i] * 2, w[i], d[i]] for i in range(N)], key = lambda t: [-t[3], -t[0]])
    broke = -2
    minx, miny, maxx, maxy = min(x) * 2, min(y) * 2, max(x) * 2, max(y) * 2
    for i in range(N):
        marbles[i] = marbles[i][1:]
    for i in range(4001):
        found = set()
        temp = []
        tminx, tminy, tmaxx, tmaxy = 2002, 2002, -2002, -2002, 
        for x, y, w, d in marbles:
            match d:
                case 'U':
                    if y == -2001:
                        continue
                    y += 1
                    if (x, y) in found:
                        broke = i
                        continue
                    elif y > maxy:
                        continue
                    else:
                        found.add((x, y))
                        temp.append((x, y, w, d))
                case 'D':
                    if y == 2001:
                        continue
                    y -= 1
                    if (x, y) in found:
                        broke = i
                        continue
                    elif y < miny:
                        continue
                    else:
                        found.add((x, y ))
                        temp.append((x, y, w, d))
                case 'L':
                    if x == -2001:
                        continue
                    x -= 1
                    if (x, y) in found:
                        broke = i
                        continue
                    elif x < minx:
                        continue
                    else:
                        found.add((x, y))
                        temp.append((x, y, w, d))
                case 'R':
                    if x == 2001:
                        continue
                    x += 1
                    if (x, y) in found:
                        broke = i
                        continue
                    elif x > maxx:
                        continue
                    else:
                        found.add((x, y))
                        temp.append((x, y, w, d))
            tminx, tminy, tmaxx, tmaxy = min(tminx, x), min(tminy, y), max(tmaxx, x), max(tmaxy, y)
        marbles = temp
        minx, miny, maxx, maxy = tminx, tminy, tmaxx, tmaxy
        if len(marbles) == 0:
            break
    print(broke + 1)