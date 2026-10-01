n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
y_val = dict()
for x, y in points:
    if x in y_val:
        y_val[x] = min(y_val[x], y)
    else:
        y_val[x] = y
print(sum(y_val.values()))