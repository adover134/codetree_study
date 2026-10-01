n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]

# Please write your code here.
word_to_num = dict()
num_to_word = dict()
for i, word in enumerate(words):
    word_to_num[word] = i
    num_to_word[i] = word
for query in queries:
    if query[0] >= '0' and query[0] <= '9':
        print(num_to_word[int(query)])
    else:
        print(word_to_num[query])