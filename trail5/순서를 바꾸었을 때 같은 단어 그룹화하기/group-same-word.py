n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
word_dict = dict()
for word in words:
    t = tuple(sorted(word))
    if t in word_dict:
        word_dict[t] += 1
    else:
        word_dict[t] = 1
print(max(word_dict.values()))