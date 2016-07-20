def solution(s):
    sum = 0
    list_char = list(s)
    roman_chars = {'M': 1000, 'C': 100, 'D': 500, 'X': 10, 'L': 50, 'I': 1, 'V': 5}
    for i, char in enumerate(list_char, 0):
        list_char[i] = roman_chars[char]
        if i == 0:
            sum = list_char[i]
        else:
            if list_char[i-1] < list_char[i]:
                sum += list_char[i] - list_char[i-1]*2
            else:
                sum += list_char[i]
    return sum


if __name__ == '__main__':
    s = 'XIV'
    print solution(s)
