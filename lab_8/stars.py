def stars(string):
    words = string.split()
    max_length = max(len(word) for word in words)
    padded_words = list(map(lambda word: word.rjust(max_length, '*'), words))
    return padded_words
