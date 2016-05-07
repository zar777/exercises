class MyQueue(object):
    """this class is created to represent a queue, given two stacks"""
    def __init__(self, stack_one, stack_two):
        self.stack_one = stack_one
        self.stack_two = stack_two

    def create_queue(self):
        """this method is created to represent a queue, given two stacks"""
        counter_position = 0
        while len(self.stack_one):
            element = self.stack_one.pop(0)
            self.stack_two.insert(0, element)
            counter_position += 1
            previous_position = counter_position - 1

        while counter_position != len(self.stack_two):
            self.stack_one.insert(0, self.stack_two[counter_position])
            counter_position += 1

        while previous_position >= 0:
            self.stack_one.insert(0, self.stack_two[previous_position])
            previous_position -= 1

        while len(self.stack_two):
            self.stack_two.pop(0)

        return self.stack_one

if __name__ == '__main__':
    stack_two = [3, 2, 5, 4]
    stack_one = ["D", "A", "B", "C"]
    my_queue = MyQueue(stack_one, stack_two)
    print my_queue.create_queue()
    print my_queue.stack_two
