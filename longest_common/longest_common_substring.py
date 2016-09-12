def longest_common_substring(a, b):
    # matrice 2D per le soluzioni: inizio tutti i valori a 0
    array2D = [[0 for x in xrange(len(a)+1)] for x in xrange(len(b)+1)]
    for i in xrange(1, len(b)+1):
        for j in xrange(1, len(a) + 1):
            # se il carattere nelle due stringhe e uguale inserisco nella matrice il valore precedente nella diagonale
            # sommato ad 1. Questo perche` il valore nella cella precedente(diagonale) sarebbe il valore che indica
            # i caratteri in comune fino a quel momento ( derivati nella iterazione precedente)
            if b[i-1] == a[j-1]:
                array2D[i][j] = array2D[i-1][j-1]+1
            else:
                array2D[i][j] = 0
    result = -1
    index_b = -1
    # ciclo per determinare la lunghezza della stringa e l'indice di dove finisce la stringa in comune
    for i in xrange(1, len(b) + 1):
        for j in xrange(1, len(a) + 1):
            if result < array2D[i][j]:
                result = array2D[i][j]
                index = i
    # prendo la porzione di stringa data da: il carattere all'indice di dove si trova l'ultimo valore in comune ed
    # a ritroso di N caratteri (result) che e` la lunghezza della substring
    return b[index_b-result:index_b]


if __name__ == '__main__':
    a = "tutorialhorizon"
    b = "dynamictutorialProgramming"
    print longest_common_substring(a, b)