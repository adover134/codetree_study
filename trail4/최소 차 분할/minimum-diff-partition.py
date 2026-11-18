n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# 각 수를 더해 가면서
# 합이 절반을 넘지 않는 최댓값을 구한다.
s = sum(arr)
p = s // 2
from collections import deque
# 합, 다음 인덱스
maxi = 0
dp = [False for _ in range(p + 1)]
dp[0] = True
for i in range(n):
    t = [False for _ in range(p + 1)]
    for d in range(p + 1 - arr[i]):
        if dp[d]:
            t[d + arr[i]] = True
    for d in range(p + 1):
        dp[d] |= t[d]
for i in range(p, -1, -1):
    if dp[i]:
        print(s - i * 2)
        exit(0)