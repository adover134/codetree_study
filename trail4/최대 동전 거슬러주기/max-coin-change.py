N, M = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.
coin = sorted([c for c in coin if c <= M])
cnt = [-1]*(M+1)
for c in coin:
    cnt[c] = 1
for m in range(1, M+1):
    t = [cnt[m-c] for c in coin if m >= c and cnt[m-c] > 0]
    if t:
        cnt[m] = max(t)+1
if cnt[M] == 0:
    print(-1)
else:
    print(cnt[M])