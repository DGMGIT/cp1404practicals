"""
CP1404/CP5632 Practical
word occurrences
Daniel Mackenzie
"""

word_to_count = {}

user_input = input("Text: ")
words = user_input.split()
for word in words:
    if word in word_to_count:
        word_to_count[word] =+ 1
    else:
        word_to_count[word] = 1


words = list(word_to_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))

#the fish jumps over the dragons gate