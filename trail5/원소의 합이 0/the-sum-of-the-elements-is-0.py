n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

# Please write your code here.
ab = dict()
cd = dict()
for a in A:
    for b in B:
        if (a + b) in ab:
            ab[a + b] += 1
        else:
            ab[a + b] = 1
for c in C:
    for d in D:
        if (c + d) in cd:
            cd[c + d] += 1
        else:
            cd[c + d] = 1
ans = 0
for num in ab:
    if -num in cd:
        ans += ab[num] * cd[-num]
print(ans)