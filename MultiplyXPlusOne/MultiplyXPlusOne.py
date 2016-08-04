# def solution(s, t, count):
#     if s > t:
#         return -1
#     if t == s:
#         return count
#     t -= 1
#     if t % 3 == 0 and t % 2 == 0:
#         solution(s, t / 3, count + 1)
#         solution(s, t / 2, count + 1)
#     if t % 3 == 0:
#         return solution(s, t/3, count+1)
#     elif t % 2 == 0:
#         return solution(s, t / 2, count+1)

def solution(s, t, count):
    while
        if s > t:
            return -1
        if t == s:
            return count
        t -= 1
        if t % 3 == 0 and t % 2 == 0:
            solution(s, t / 3, count + 1)
            solution(s, t / 2, count + 1)
        if t % 3 == 0:
            return solution(s, t/3, count+1)
        elif t % 2 == 0:
            return solution(s, t / 2, count+1)


if __name__ == '__main__':
    print solution(1, 31, 0)