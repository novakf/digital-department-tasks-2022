words_count = {}
words=input().split(', ')
for word in words:
    if words_count.get(word):
        words_count[word]+=1
    else:
        words_count[word]=1

top_counts=sorted(words_count.values(), reverse=True)

top_three_counts = top_counts[:3]

for count in top_three_counts:
    for value in words_count:
        if words_count[value]==count:
            print(f'{value}: {count}')