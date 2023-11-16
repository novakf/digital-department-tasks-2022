s = input()
s1 = input()
a = s.split()
for word in a:
    low_word=word.lower()
    if s1 in low_word:
        print(word)