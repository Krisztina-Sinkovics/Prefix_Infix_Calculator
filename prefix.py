from helpers import Stack, parse_expression, is_number


def evaluate_prefix_notation(expr):
    """
    Evaluate a given expression in prefix notation.
    """
    expression = parse_expression(expr)
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
    test_expression1 = "+ 9 * 2 6"
    print(evaluate_prefix_notation(test_expression1))

    test_expression2 = "3"
    print(evaluate_prefix_notation(test_expression2))

    test_expression3 = "+ 1 2"
    print(evaluate_prefix_notation(test_expression3))

    test_expression4 = "+ 1 * 2 3"
    print(evaluate_prefix_notation(test_expression4))

    test_expression5 = "+ * 1 2 3"
    print(evaluate_prefix_notation(test_expression5))

    test_expression6 = "- / 10 + 1 1 * 1 2"
    print(evaluate_prefix_notation(test_expression6))

    test_expression7 = "- 0 3"
    print(evaluate_prefix_notation(test_expression7))

    test_expression8 = "/ 3 2"
    print(evaluate_prefix_notation(test_expression8))

    test_expression8 = "/ 3 0"
    print(evaluate_prefix_notation(test_expression8))
