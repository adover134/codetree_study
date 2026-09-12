N, M = map(int, input().split())
coin = list(map(int, input().split()))

# Please write your code here.
coin = sorted([c for c in coin if c <= M], reverse = True)
dp=[100001 for _ in range(M+1)]
for c in coin:
    dp[c] = 1
from collections import deque
from copy import deepcopy
dq = deque(deepcopy(coin))
while dq:
    x = dq.popleft()
    for c in coin:
        if (x+c)<=M:
            if dp[x+c] > dp[x]+1:
                dp[x+c] = dp[x]+1
                dq.append(x+c)
if dp[-1] == 100001:
    print(-1)
else:
    print(dp[-1])