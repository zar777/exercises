"""Write a method to compute all permutations of a string
Failed"""
def permutations(string):

    array = []
    for c in string:
        substring = string.replace(c, "")
        array.append(c+recursive_permutations(substring))
    return array


def recursive_permutations(string):

    if string == "":
        return

     recursive_permutations()


if __name__ == '__main__':
    string = "cia"