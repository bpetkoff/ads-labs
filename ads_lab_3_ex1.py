"""
In this file are the
"Reverse stack" problem and
"Parentheses matching" problem

"""


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class ArrayStack:
    """Create an empty stack"""
    def __init__(self):
        self._data = []  # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Add element to the top of the stack"""
        self._data.append(e)  # new item stored at the end of the list

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack

        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("The stack is empty")
        return self._data[-1]

    def pop(self):
        """
        Remove and return element from the top of the stack (i.e. LIFO)

        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("The stack is empty")
        return self._data.pop()  # remove last item from the list


# This is the reveres stack problem
if __name__ == '__main__':
    s = ArrayStack()
    j = ArrayStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    print(s._data)

    def reverse_stack(input):
        while not input.is_empty():
            j.push(input.pop())
        for i in j._data:
            s.push(i)
        return s._data

    # print(s._data)
    print(reverse_stack(s))

# This is the solution from the lecture
# def is_matched(expr):
#     lefty = '({['
#     righty = ')}]'
#     S = ArrayStack()
#     for c in expr:
#         if c in lefty:
#             S.push(c)
#             print(S._data)
#         elif c in righty:
#             if S.is_empty():
#                 return False
#             if righty.index(c) != lefty.index(S.pop()):
#                 return False
#     return S.is_empty()
#
# print(is_matched(')(()){([()])}'))
# #


# This is my solution
def matching_parentheses(par1, par2):
    """
    Check if the parentheses match
    """
    if par1 == '(' and par2 == ')':
        return True
    if par1 == '[' and par2 == ']':
        return True
    if par1 == '{' and par2 == '}':
        return True
    else:
        return False

def matched(expr):
    S = ArrayStack()
    for c in expr:
        if c in '({[':
            S.push(c)
        elif c in ')}]':
            if S.is_empty():
                return False
            else:
                j = S.pop()
                print(j)
                print(c)
                valid = matching_parentheses(j, c)
                if not valid:
                    return False
    return S.is_empty()


print(matched(')(()){([()])}'))
