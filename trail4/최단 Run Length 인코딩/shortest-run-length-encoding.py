A = input()

# Please write your code here.
# 가능한 한, 알파벳들이 뭉쳐 있는 것이 좋다.
# 다만, 그냥 매번 shift하는 게 나을 수 있다.
maxi = 0
for i in range(len(A)):
    a = A[i:]+A[:i]
    s = 1
    t = 0
    for j in range(1, len(A)):
        if a[j] == a[j-1]:
            s += 1
        else:
            t += 1+len(str(s))
            s = 1
    if t == 0:
        t = 1+len(str(s))
    maxi = max(t, maxi)
print(maxi)