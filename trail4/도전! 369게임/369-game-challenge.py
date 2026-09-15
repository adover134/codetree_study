import sys

sys.setrecursionlimit(100000)

n = input()

# Please write your code here.
# digit DP 문제인가?
# 각 자리가 3 / 6 / 9 중 하나이며
# 3의 배수가 아닌 경우 쳐야 된다.

# 3 6 9 12 15 18 21 24 27
# 13 16 19 23 26 29
# 9 + 6 + 4 = 19

# 각 숫자는 딱 한 번씩만 치면 된다.

# 3의 배수 중 3이 들어가는 경우의 수?
# 3, 30, 33, 36, 39, 63, 93, ...
# 현재 위치에서 3이 나타나면 그 이하의 모든 수는 박수
# 이외의 경우, 3의 배수인 경우에만.
n = list(map(int, str(n)))
ln = len(n)
# dp[i][j][k]는 합을 3으로 나눈 나머지가 i이며, 3의 배수가 나타난 적이 있는가는 j
# k가 0이면 lock 여부 (0이면 lock==False)
dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(3)]
dp[0][0][1] = 1

for n_ in n:
    t = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(3)]
    # 합이 3의 배수였는가
    for s in range(3):
        # 3이 나온 적이 있는가
        for m in range(2):
            # lock 여부
            for k in range(2):
                cnt = dp[s][m][k]
                if cnt == 0:
                    continue
                limit = n_ if k == 1 else 9
                # lock이 되어 있다면
                # 우선은 lock이 안 걸리는 범위부터
                for num in range(limit + 1):
                    ss = (s+num) % 3
                    mm = 1 if (num in {3, 6, 9} or m == 1) else 0
                    kk = 1 if ((k==1) and (num==limit)) else 0
                    t[ss][mm][kk]=(t[ss][mm][kk]+cnt)%1000000007
                    
    dp = t

ans = 0            
for s in range(3):
    for m in range(2):
        if s == 0 or m == 1:
            ans += sum(dp[s][m])

print((ans - 1) % 1000000007)