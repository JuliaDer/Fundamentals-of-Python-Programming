in_file = open("input.txt", "r", encoding="utf8")
counter = {}
for word in in_file.read().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
