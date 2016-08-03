def solution(a):
    count = 0
    result = 1
    for el in a[0: (len(a)/2)]:
        result *= el
    result *= 40
    while result > 0:
        if result % 2 == 0:
            for element in a[(len(a)/2): len(a)+1]:
                if count == len(a)/2:
                    return result
                if result % element == 0:
                    count += 1
                else:
                    count = 0
                    result += 1
                    break
        else:
            result +=1



if __name__ == '__main__':
    a = range(1, 21)
    print solution(a)