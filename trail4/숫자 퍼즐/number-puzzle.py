n, m, k = map(int, input().split())

# Please write your code here.
# digit DP 문제인가?
# 숫자 합은 반드시 M
# 2자리 숫자에 대해
# 합이 M이어야 하는 경우 가능한 개수를 구하자.
# 합 / 개수가 줄어든 경우를 구해야 하는데

dp = [[[-float('inf') for _ in range(m+1)] for _ in range(m+1)] for _ in range(n + 1)]

# pos: 이번 위치
# mini: 직전 위치에서 선택한 최솟값
# M: 남은 합
# dp[pos][mini][M]은 pos번째 숫자로 mini를 골랐고, pos를 포함해서 이후까지 합이 mini여야 한다.

def fill_dp(pos, prev, M):
    # pos 위치에 prev를 넣은 상태에서 나머지를 채울 수 있는 가짓수를 구하는 것이 목표이다.
    # 값은 prev 이상이어야 한다.
    # 남은 수는 M-prev이다.
    remaining = M-prev

    if pos == (n-1):
        if remaining == 0:
            return 1
        else:
            return 0
    
    s = 0
    # pos + 1 위치에는
    # prev 이상의 수만 들어갈 수 있다.

    # pos + 1 위치에 i를 넣을 때
    for i in range(prev, remaining+1):
        global dp
        # 다음 위치는 pos+1
        # 다음 최소값은 i
        # 다음 M은 remaining
        if dp[pos+1][i][remaining] == -float('inf'):
            dp[pos+1][i][remaining] = fill_dp(pos+1, i, remaining)
        s += dp[pos+1][i][remaining]
    return s
for i in range(m+1):
    dp[0][i][m] = fill_dp(0, i, m)

s = 0
i = 0
j = 1
M = m

ans = []

while s < k:
    if s + dp[i][j][M] >= k:
        ans.append(str(j))
        if i < (n-1):
            i += 1
            M -= j
        else:
            break
    else:
        if dp[i][j][M] > 0:
            s += dp[i][j][M]
        j += 1
    if i == n or j > M or M < 0:
        break
print(' '.join(ans))