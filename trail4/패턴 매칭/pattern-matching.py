s = input()
p = input()

# Please write your code here.
# dp[i][j]는
# s[:i+1]이 p[:j+1]에 대응하는가를 본다.
# 만약 dp[i-1][j]가 True이고, p[j]가 '*'이라면
# dp[i][j]도 True
# 만약 dp[i-1][j-1]이 True이고, p[j]가 '.'이라면
# dp[i][j]도 True
# 만약 dp[i-1][j-1]이 True이고, s[i]와 p[j]가 같다면
# dp[i][j]도 True
t = []
i = 0
lp = len(p)
while i < lp:
    if i < (lp - 1) and p[i+1] == '*':
        t.append(p[i:i+2])
        i += 2
    else:
        t.append(p[i])
        i += 1
p = t
ls, lp = len(s), len(p)
dp = [[False for _ in range(ls+1)] for _ in range(lp+1)]
dp[0][0] = True
for j in range(1, lp+1):
    for i in range(1, ls+1):
        if len(p[j-1]) > 1:
            if ((dp[j][i-1] or dp[j-1][i-1]) and (s[i-1]==p[j-1][0] or p[j-1][0] == '.')) or dp[j-1][i]:
                dp[j][i] = True
        elif p[j-1] == '.':
            if dp[j-1][i-1]:
                dp[j][i] = True
        else:
            if p[j-1] == s[i-1] and dp[j-1][i-1]:
                dp[j][i] = True
if dp[lp][ls]:
    print('true')
else:
    print('false')