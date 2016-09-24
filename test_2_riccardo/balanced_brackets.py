"""1. Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of
opening/closing brackets (in that order), none of which mis-nest.

Examples:

   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK """


def is_balanced(s):
    stack = []
    for bracket in s:
        if bracket == "[":
            stack.append(bracket)
        elif stack:
            stack.pop()
    if stack:
        return False
    else:
        return True

if __name__ == '__main__':
    a = "[]"
    b = "[][]"
    c = "[[][]]"
    d = "]["
    e = "][]["
    f = "[]][[]"
    print is_balanced(f)
