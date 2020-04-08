Sentence = input('Enter Sentence: ')
str = Sentence.split(' ')
WordCount = {}
for word in str:
    if word in WordCount:
        WordCount[word] += 1
    else:
        WordCount[word] = 1
print(WordCount)
for k, v in WordCount.items():
    print(k,'-->',v)

