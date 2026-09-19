n = int(input())
x1, x2 = [], []
lines = sorted(list(tuple(map(int, input().split())) for _ in range(n)))

# Please write your code here.
# 선분들을 먼저 정렬한다.
# 그 뒤에 고르면 된다.
end = -1
start = -1
ans = 0
for s, e in lines:
    if start == s:
        continue
    if end < s:
        ans += 1
        start = s
        end = e
    elif end > e:
        start = s
        end = e
print(ans)