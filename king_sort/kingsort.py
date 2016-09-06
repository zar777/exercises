kings = ["Philippe VI", "Jean II", "Charles V", "Charles VI", "Charles VII", "Louis XI"]

def roman_to_int(number):
    m = {
        'II': 2,
        'V': 5,
        'VI': 6,
        'VII': 7,
        'XI': 11
    }
    return m[number]


def sorter(s1, s2):
    king1 = s1.split()
    king2 = s2.split()
    if king1[0] < king2[0]:
        return -1
    elif king1[0] == king2[0]:
        a = roman_to_int(king1[1])
        b = roman_to_int(king2[1])
        if a < b:
            return -1
        elif a > b:
            return 1
    return 0


print sorted(kings, cmp=sorter)