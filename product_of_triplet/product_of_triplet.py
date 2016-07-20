def solution(A):
    A.sort(reverse=True)
    prod_tree_positive = A[0]*A[1]*A[2]
    prod_tree_negative = A[0]*A[len(A)-2]*A[len(A)-1]
    if prod_tree_negative <= prod_tree_positive:
        return prod_tree_positive
    else:
        return prod_tree_negative


if __name__ == '__main__':
     A = [-5, 5, -5, 4]
     print solution(A)