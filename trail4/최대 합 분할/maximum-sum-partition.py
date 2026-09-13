n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
m = sum(arr)
# 만들 수 있는 모든 subset을 구한 뒤
# 나머지에서 동일한 합이 가능한지 보기?

# i번째 수까지 봤을 때
# 두 그룹 사이의 차이가 0인 경우 구하기?

# 전체 최대 합은 100000
# i번째 행에서의 값은
# A/B 차이가 j일 때 A의 합?
offset = m+1
import sys
INT_MIN = -sys.maxsize
dp=[
    [0] * (m+offset+1) for _ in range(n+1)
]
for i in range(n+1):
    for j in range(-m+offset, m+offset+1):
        dp[i][j] = INT_MIN
dp[0][offset] = 0
for i in range(1,n+1):
    for j in range(-m+offset, m+offset):
        # C에 더한 경우
        a=dp[i-1][j]
        # A에 더한 경우
        if (j-arr[i-1])>=0:
            b=dp[i-1][j-arr[i-1]]
        else:
            b=INT_MIN
        # B에 더한 경우
        if (j+arr[i-1])<=(m+offset):
            c=dp[i-1][j+arr[i-1]]
        else:
            c=INT_MIN
        # A에 더한 경우만 추가해서
        dp[i][j] = max([a,b+arr[i-1],c])
print(dp[-1][offset])
