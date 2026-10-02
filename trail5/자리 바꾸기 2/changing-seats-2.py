n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
'''
각 사람마다 set을 두고
배열에는 각 사람들을 둔 뒤에 그 위치가 바뀌면 옮기기?
'''
pos = [set([i]) for i in range(1 + n)]
cur = [i for i  in range(1 + n)]
for _ in range(3):
    for a, b in edges:
        f, s = cur[a], cur[b]
        pos[f].add(b)
        pos[s].add(a)
        cur[a], cur[b] = s, f
for p in range(1, n + 1):
    print(len(pos[p]))