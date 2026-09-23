N = int(input())
r, c = map(int, input().split())

grid = [["."] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = input()
    for j in range(1, N + 1):
        grid[i][j] = row[j - 1]

# Please write your code here.
d = 0
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
cnt = 0
visited = set()
visited.add((r, c, d))
# 시작 위치 오른쪽에는 항상 벽이 있다.
while c > 0 and r > 0 and c < (N + 1) and r < (N + 1):
    # 오른쪽 칸
    rr, rc = r + dr[(d + 1) % 4], c + dc[(d + 1) % 4]
    # 오른쪽에 벽이 있는 동안 전진
    if grid[rr][rc] == '#':
        ar, ac = r + dr[d], c + dc[d]
        if ar > 0 and ar < (N + 1) and ac > 0 and ac < (N + 1) and grid[r + dr[d]][c + dc[d]] == '#':
            d = (d + 3) % 4
            if (r, c, d) not in visited:
                visited.add((r, c, d))
            else:
                break
        else:
            r, c = r + dr[d], c + dc[d]
            cnt += 1
            if (r, c, d) in visited:
                break
            visited.add((r, c, d))
    # 없다면 우회전 후 전진
    else:
        # 우선 우회전을 한 뒤
        ad = (d + 1) % 4
        # 추가 이동이 가능할 때까지 회전
        for i in range(3):
            if grid[r + dr[ad]][c + dc[ad]] == '#':
                ad = (ad + 1) % 4
            else:
                break
        if ad == d:
            break
        else:
            d = ad
        if (r + dr[d], c + dc[d], d) in visited:
            break
        else:
            r, c = r + dr[d], c + dc[d]
            visited.add((r, c, d))
            cnt += 1
if r <= 0 or c <= 0 or r > N or c > N:
    print(cnt)
else:
    print(-1)