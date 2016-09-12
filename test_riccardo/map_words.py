def map_words(words, way):
    if way == 'l':
        result = []
        for word in words:
            result.append(len(word))
        return result
    elif way == 'm':
        a = map(lambda word: len(word), words)
        return a
    elif way == 'c':
        return [len(word) for word in words]


if __name__ == '__main__':
    words = ['ciao', 'sono', 'riccardo', 'il', 'puttaniere', 'bastardo']
    print map_words(words, 'm')