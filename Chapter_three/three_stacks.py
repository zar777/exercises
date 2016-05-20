"""Describe how you could use a single array to implement three stacks. Exercises 3.1
    I WRONG BECAUSE I USE A LIST AND NOT AN ARRAY"""
class ThreeStacks(object):
    """this class is created to represent an empty array which there are only two divisors used by
     delimited the three stacks"""
    def __init__(self):
        self.array = ["Divisor_one", "Divisor_two"]


    def push_first_stack(self, element):
        "push element in the first stack"
        self.array.insert(0, element)

    def push_second_stack(self, element):
        "push element in the second stack"
        self.array.insert(self.array.index("Divisor_one") + 1, element)

    def push_third_stack(self, element):
        "push element in the third stack"
        self.array.insert(self.array.index("Divisor_two") + 1, element)

    def pop_first_stack(self):
        "pop element in the first stack"
        if self.array[0] != "Divisor_one":
            self.array.pop(0)

    def pop_second_stack(self):
        "pop element in the second stack"
        if self.array[self.array.index("Divisor_one") + 1] != "Divisor_two":
            self.array.pop(self.array.index("Divisor_one") + 1)

    def pop_third_stack(self):
        "pop element in the third stack"
        if self.array.index("Divisor_two") + 1 != len(self.array):
            self.array.pop(self.array.index("Divisor_two") + 1)


if __name__ == '__main__':
    three_stack = ThreeStacks()
    three_stack.pop_first_stack()
    three_stack.pop_second_stack()
    three_stack.pop_third_stack()
    print three_stack.array
    three_stack.push_first_stack(2)
    three_stack.push_first_stack(4)
    three_stack.push_first_stack(8)
    print three_stack.array
    three_stack.push_second_stack(55)
    three_stack.push_second_stack(33)
    three_stack.push_second_stack(22)
    three_stack.push_second_stack(1)
    print three_stack.array
    three_stack.push_third_stack(99)
    three_stack.push_third_stack("A")
    print three_stack.array
    three_stack.pop_first_stack()
    three_stack.pop_second_stack()
    three_stack.pop_third_stack()
    print three_stack.array
    three_stack.pop_first_stack()
    three_stack.pop_second_stack()
    three_stack.pop_third_stack()
    print three_stack.array
    three_stack.pop_first_stack()
    three_stack.pop_first_stack()
    three_stack.pop_first_stack()
    print three_stack.array




