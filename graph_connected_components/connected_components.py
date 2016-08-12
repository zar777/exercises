def zombies(adj_matrix):
    visited = set()
    n_components = 0
    for i in xrange(len(adj_matrix)):
        if i not in visited:
            component = {i}
            to_visit = [i]
            while len(to_visit) > 0:
                j = to_visit.pop(0)
                for k, is_connected in enumerate(adj_matrix[j]):
                    if k != j and bool(int(is_connected)) and k not in component:
                        component.add(k)
                        to_visit.append(k)
                visited.add(j)
            n_components += 1
    return n_components


if __name__ == '__main__':
    matrix = ['11000',
              '11100',
              '01100',
              '00011',
              '00011']
    print zombies(matrix)
    matrix = ['1100',
              '1110',
              '0110',
              '0001']
    print zombies(matrix)
    matrix = ['10000',
              '01000',
              '00100',
              '00010',
              '00001']
    print zombies(matrix)