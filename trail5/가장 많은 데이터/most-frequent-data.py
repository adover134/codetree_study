n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
maxi = 0
hashmap = dict()
for word in words:
    if word in hashmap:
        hashmap[word] += 1
    else:
        hashmap[word] = 1
    maxi = max(hashmap[word], maxi)
print(maxi)