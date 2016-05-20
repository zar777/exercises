"""Write a program to sort a stack in ascending order. You should not make any assump-
tions about how the stack is implemented. The following are the only functions that
should be used to write this program: push | pop | peek | isEmpty. exercises 3.6"""
class SortStack(object):
    def __init__(self, list):
        self.list = list

    def push(self, x):
        self.list.insert(0, x)

    def pop(self):
        return self.list.pop()

    def is_empty(self):

        if len(self.list) == 0:
            return True
        else:
            return False

    def peek(self):
        return self.list[0]

    def sort_ascending(self):
        sort = SortStack([])

        while self.is_empty() is False:
            first = self.pop()
                while sort.is_empty() is False and sort.peek() > first:
                sort.push(first)
            else:
                pass

"""Failed"""
if __name__ == '__main__':
    a = []
    stack = SortStack(a)
    a.insert(0, 1)
    a.insert(0, 2)
    a.append(3)