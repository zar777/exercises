

def solution(A):
    points_circle = []
    for el, i in enumerate(A, 0):
        points_circle.append([i+A[i], i-A[i]])
    for el in points_circle:
        if 
    return points_circle


if __name__ == '__main__':
    A = [1, 5, 2, 1, 4, 0]
    print solution(A)