T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    x, y, d = [], [], []
    for _ in range(M):
        xi, yi, di = input().split()
        x.append(int(xi))
        y.append(int(yi))
        d.append(di)

    # Please write your code here.
    # 총 2N 시간이면 모든 구슬이 한 번 왕복하니
    # 그 시간 동안 살아남았다면 생존한 거다.
    # 필요한 건, 각 구슬의 위치와
    # 현재까지 구슬이 놓인 위치들이다.
    marbles = list(zip(x, y, d))
    for i in range(N*2):
        found = set()
        temp = set()
        for x, y, d in marbles:
            match d:
                case 'L':
                    ax, ay = x, y - 1
                    if ay == 0:
                        ay, d = y, 'R'
                    if (ax, ay) in found:
                        if (ax, ay, 'L') in temp:
                            temp.remove((ax, ay, 'L'))
                        if (ax, ay, 'R') in temp:
                            temp.remove((ax, ay, 'R'))
                        if (ax, ay, 'U') in temp:
                            temp.remove((ax, ay, 'U'))
                        if (ax, ay, 'D') in temp:
                            temp.remove((ax, ay, 'D'))
                    else:
                        temp.add((ax, ay, d))
                        found.add((ax, ay))
                case 'R':
                    ax, ay = x, y + 1
                    if ay == (N + 1):
                        ay, d = y, 'L'
                    if (ax, ay) in found:
                        if (ax, ay, 'L') in temp:
                            temp.remove((ax, ay, 'L'))
                        if (ax, ay, 'R') in temp:
                            temp.remove((ax, ay, 'R'))
                        if (ax, ay, 'U') in temp:
                            temp.remove((ax, ay, 'U'))
                        if (ax, ay, 'D') in temp:
                            temp.remove((ax, ay, 'D'))
                    else:
                        temp.add((ax, ay, d))
                        found.add((ax, ay))
                case 'U':
                    ax, ay = x - 1, y
                    if ax == 0:
                        ax, d = x, 'D'
                    if (ax, ay) in found:
                        if (ax, ay, 'L') in temp:
                            temp.remove((ax, ay, 'L'))
                        if (ax, ay, 'R') in temp:
                            temp.remove((ax, ay, 'R'))
                        if (ax, ay, 'U') in temp:
                            temp.remove((ax, ay, 'U'))
                        if (ax, ay, 'D') in temp:
                            temp.remove((ax, ay, 'D'))
                    else:
                        temp.add((ax, ay, d))
                        found.add((ax, ay))
                case 'D':
                    ax, ay = x + 1, y
                    if ax == (N + 1):
                        ax, d = x, 'U'
                    if (ax, ay) in found:
                        if (ax, ay, 'L') in temp:
                            temp.remove((ax, ay, 'L'))
                        if (ax, ay, 'R') in temp:
                            temp.remove((ax, ay, 'R'))
                        if (ax, ay, 'U') in temp:
                            temp.remove((ax, ay, 'U'))
                        if (ax, ay, 'D') in temp:
                            temp.remove((ax, ay, 'D'))
                    else:
                        temp.add((ax, ay, d))
                        found.add((ax, ay))
        marbles = list(temp)
    print(len(marbles))
        