words = ("apple", "banana", "strawberry", "kiwi")
word = len(words[0])
new_word = []

for i in words:
    if word < len(i):
        new_word = i
print(new_word)
        