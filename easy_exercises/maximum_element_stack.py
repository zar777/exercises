import sys


lines = sys.stdin.readline()
stack = []
stack_max = []
for query in sys.stdin:
    line = query.strip().split(" ")
    if line[0] == '1':
        number = int(line[1])
        stack.append(number)
        if stack_max:
            if stack_max[-1] <= number:
                stack_max.append(number)
        else:
            stack_max.append(number)
    elif line[0] == '2':
        pop_el = stack.pop()
        if stack_max and pop_el == stack_max[-1]:
            stack_max.pop()
    else:
        if stack:
            print stack_max[-1]