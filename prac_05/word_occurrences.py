words_in_text = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = words_in_text.get(word, 0)
    words_in_text[word] = frequency + 1

words = list(words_in_text.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} = {}".format(word, max_length, words_in_text[word]))