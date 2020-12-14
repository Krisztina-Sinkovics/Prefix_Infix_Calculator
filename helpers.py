from pip._vendor.distlib.compat import raw_input

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def parse_expression(expr):
    """
    :param expr: string with elements separated by single spaces
    :return: list of elements
    """
    expr = expr.strip()
    expr = expr.split(' ')
    return expr


def is_number(el):
    """
    Return True if the element is is a number
    """
    return el.isdigit()


def is_operator(el):
    """
    Return True if the element is is an operator
    """
    return el in ['+', '-', '*', '/']
