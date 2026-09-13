n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
A=sorted([a for a in A if a <= m],reverse=True)
found=[False]*(m+1)
for num in A:
    for i in range(m,num,-1):
        if found[i-num]:
            found[i]=True
    found[num]=True
if found[m]:
    print('Yes')
else:
    print('No')