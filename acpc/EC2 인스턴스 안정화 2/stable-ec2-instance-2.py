N = int(input())
A = list(map(int, input().split()))

# 둘 선택 후 버스트 모드가 된다면
# 두 인스턴스는 성능이 2배가 된다.

# 그 후 안정성 점수를 계산하는데
# 인접 사이의 차이의 절댓값의 총합이다.
# 가능한 모든 경우를 구하면 되는데

# 2개씩 차이를 미리 구해 둔다.
# i를 바꾸면
# i 주변의 값과
# j 주변의 값만 바뀐다.

def get_score(scores):
    score = 0
    for i in range(N - 1):
        score += abs(scores[i] - scores[i + 1])
    return score

base = 0
for i in range(N - 1):
    base += abs(A[i] - A[i + 1])
maxi = -5005
for i in range(N - 1):
    t1 = 0
    if i == 0:
        t1 -= abs(A[0] - A[1])
        t1 += abs(A[0] * 2 - A[1])
    else:
        t1 -= abs(A[i] - A[i - 1]) + abs(A[i] - A[i + 1])
        t1 += abs(A[i] * 2 - A[i - 1]) + abs(A[i] * 2 - A[i + 1])
    A[i] *= 2
    for j in range(i + 1, N):
        t2 = 0
        if j == (N - 1):
            t2 -= abs(A[N - 1] - A[N - 2])
            t2 += abs(A[N - 1] * 2 - A[N - 2])
        else:
            t2 -= abs(A[j] - A[j - 1]) + abs(A[j] - A[j + 1])
            t2 += abs(A[j] * 2 - A[j - 1]) + abs(A[j] * 2 - A[j + 1])
        if (t1 + t2) > maxi:
            maxi = (t1 + t2)
    A[i] //= 2
print(maxi + base)


# 1 4 3 20 => 3 1 17 => 21
# t1: -2 + 4 = 2
# t2 = -7 + 17 = 10
# base = 1 + 1 + 7 = 9