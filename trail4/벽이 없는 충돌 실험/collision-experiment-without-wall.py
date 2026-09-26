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
    marbles = sorted([[i, x[i] * 2, y[i] * 2, w[i], d[i]] for i in range(N)], key = lambda t: [-t[3], -t[0]])
    broke = -2
    for i in range(N):
        marbles[i] = marbles[i][1:]
    for i in range(4001):
        found = set()
        temp = []
        for x, y, w, d in marbles:
            match d:
                case 'U':
                    if y == 2001:
                        continue
                    if (x, y + 1) in found:
                        broke = i
                        continue
                    else:
                        found.add((x, y + 1))
                        temp.append((x, y + 1, w, d))
                case 'D':
                    if y == -2001:
                        continue
                    if (x, y - 1) in found:
                        broke = i
                        continue
                    else:
                        found.add((x, y - 1))
                        temp.append((x, y - 1, w, d))
                case 'L':
                    if x == -2001:
                        continue
                    if (x - 1, y) in found:
                        broke = i
                        continue
                    else:
                        found.add((x - 1, y))
                        temp.append((x - 1, y, w, d))
                case 'R':
                    if x == 2001:
                        continue
                    if (x + 1, y) in found:
                        broke = i
                        continue
                    else:
                        found.add((x + 1, y))
                        temp.append((x + 1, y, w, d))
        marbles = temp
    print(broke + 1)
