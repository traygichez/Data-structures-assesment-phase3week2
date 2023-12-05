def word_frequency(sentence):
    words = [split_word.strip(',.!?').lower() for split_word in sentence.split()]
    return {word: words.count(word) for word in words}

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)