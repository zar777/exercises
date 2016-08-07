class BracketSequenceDiv1(object):

    def verify_validity(self, array):
        stack = []
        for bracket in array:
            if bracket == "(" or bracket == "[":
                stack.append(bracket)
            elif len(stack) != 0:
                if (bracket == "]" and stack[len(stack)-1] == "[") or (bracket == ")" and stack[len(stack)-1] == "("):
                    stack.pop()
                else:
                    return 0
            else:
                return 0
        if len(stack) != 0:
            return 0
        else:
            return 1

    def count(self, s):
        # split_string = list(s)
        counter = 0
        for index in xrange(0, len(s)):
            replace_string = s[:index] + s[index:index + 1].replace(s[index], "") + s[index + 1:]
            counter += self.verify_validity(replace_string)
            if index != len(s)-1:
                counter += self.verify_validity(s[index:])
            if index != 0:
                counter += self.verify_validity(s[: index])
        return counter




if __name__ == '__main__':
    s = "([)]"
    # s_list = list("())")
    brackets = BracketSequenceDiv1()
    print brackets.count(s)
    # print brackets.verify_validity(s)
