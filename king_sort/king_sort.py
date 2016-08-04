def get_sorted_list(kings):
    roman_translation = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
    list_names = []
    for index, el in enumerate(kings, 0):
        split_name = el.split(" ")
        list_names.append((split_name[0], split_name[1]))
    roman_int = {}
    new_kings = []
    for index, el in enumerate(list_names, 0):
        number = translation(roman_translation, el[1])
        king_name = el[0] + " " + number
        new_kings.append(king_name)
        roman_int[number] = el[1]
    new_kings.sort()
    final_kings = []
    for el in new_kings:
        name = el.split(" ")
        if name[1] in roman_int:
            final_kings.append(name[0] + " " + roman_int[name[1]])
    return final_kings


def translation(roman_translation, roman_number):
    sum = 0
    single_char = list(roman_number)
    int_char = []
    for char in single_char:
        if char in roman_translation:
            int_char.append(roman_translation[char])
    for index, el in enumerate(int_char, 0):
        sum += el
        if int_char[index-1] < el and index != 0:
            sum -= int_char[index-1]*2
    return str(sum)


if __name__ == '__main__':
    kings = ["Philippe VI", "Jean II", "Charles V", "Charles VI", "Charles VII", "Louis XI"]
    # roman_translation = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
    # print translation(roman_translation, "XLVII")
    print get_sorted_list(kings)