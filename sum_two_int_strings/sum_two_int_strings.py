def sum_two_int_strings(string_one, string_two):
    if len(string_one) > len(string_two):
        int_list = map(int, string_one)
        sum_string = string_two
    else:
        int_list = map(int, string_two)
        sum_string = string_one
    carry = 0
    index_char = len(sum_string)-1
    for index, char in reversed(list(enumerate(int_list))):
        if carry == 1 and index_char == -1:
            local_sum = char + carry
            int_list[index] = local_sum % 10
        elif index_char >= 0:
            local_sum = int(sum_string[index_char]) + char + carry
            int_list[index] = local_sum % 10
        carry = local_sum / 10
        if index_char >= 0:
            index_char -= 1
    if carry == 1:
        int_list.insert(0, carry)
    result = ''.join(str(x) for x in int_list)
    return result

if __name__ == '__main__':
    A = "4579"
    B = "213"
    print sum_two_int_strings(A, B)

