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
dp = {0}
for i in range(n):
    t = set()
    for d in dp:
        if (d + arr[i]) <= p:
            t.add(d + arr[i])
    dp = dp.union(t)
t = max(dp)
print(s - t * 2)