N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.
values = [0]*(M+1)
for m in range(1, M+1):
    t = values[m]
    for W, V in zip(w, v):
        if m >= W:
            t = max((values[m-W]+V), t)
    values[m] = max(values[m], t)
print(max(values))