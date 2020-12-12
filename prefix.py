from pip._vendor.distlib.compat import raw_input

from helpers import Stack, parse_expression, is_number


def evaluate_prefix_notation(expression):
    """
    Evaluate a given expression in prefix notation.
    """
    expression = parse_expression(expression)
    stack = Stack()

    # iterate from the end to start
    for el in expression[::-1]:

        # push number to stack
        if is_number(el):
            stack.push(int(el))

        else:
            # if operator pop two last numbers from stack
            value1 = stack.pop()
            value2 = stack.pop()

            # calculate the result for these two numbers
            # push the result onto the stack again
            if el == '+':
                stack.push(value1 + value2)

            elif el == '-':
                stack.push(value1 - value2)

            elif el == '*':
                stack.push(value1 * value2)

            elif el == '/':
                try:
                    stack.push(value1 / value2)
                except ZeroDivisionError:
                    return "You can't divide by zero!"

    return stack.peek()


if __name__ == "__main__":
    print("Enter expression in prefix notation, elements shoudld be space separated:")
    expr = raw_input()
    print(evaluate_prefix_notation(expr))
