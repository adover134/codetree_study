N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.
# 각 무게에 대해
# 금액 합의 최대를 구한다.
# 무게를 기준으로 정렬하는 게 좋겠어.
# 무게 역순으로 가자.
# 무게 합이 M 이하인 모든 경우를 구한 뒤
# 그 중 가장 가치가 큰 것을 반환하면 되잖아?

jewels = sorted([tuple(j) for j in zip(w, v) if j[0] <= M])

values = [0]*(M+1)
from copy import deepcopy

for w, v in jewels:
    t = deepcopy(values)
    for m in range(1, M+1):
        if (w+m)<=M and values[m]>0:
            values[w+m] = max(values[w+m], t[m]+v)
    values[w] = max(values[w], v)
print(max(values))