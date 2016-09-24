
def map_words(words, way):
    result = []
    if way == 'l':
        for word in words:
            result.append(len(word))
        return result
    elif way == 'm':
        result = map(lambda word: len(word), words)
        return result
    elif way == 'c':
        return [len(word) for word in words]
    else:
        raise ValueError("Wrong way option, please enter the correct way char")


if __name__ == '__main__':
    words = ['ciao', 'sono', 'riccardo', 'il', 'puttaniere', 'bastardo']
    print map_words(words, 'c')