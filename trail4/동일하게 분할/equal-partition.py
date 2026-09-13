n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# i번 요소를 넣었을 때
# 차이가 j인 경우가 있는가?

# offset은 100000이면 되겠어.
offset=100000
S=sum(arr)
if S%2 == 1:
    print("No")
    exit(0)
dp=[[False for i in range(S//2+1)] for _ in range(len(arr)+1)]
dp[0][0]=True
for i in range(1,len(arr)+1):
    for j in range(S//2+1):
        t=j-arr[i-1]
        if dp[i-1][j]:
            dp[i][j]=True
        if t<0:
            continue
        elif dp[i-1][t]:
            dp[i][j]=True
if dp[-1][S//2]:
    print("Yes")
else:
    print("No")