def solution(arr):
    total_square = sum(el for el in a)
    total_square *= total_square
    square_numbers = sum(el*el for el in a)
    return total_square - square_numbers


if __name__ == '__main__':
    a = range(1, 101)
    print solution(a)