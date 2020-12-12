from helpers import Stack, parse_expression, is_number, is_operator


def evaluate_infix_notation(expr):
    """
        Evaluate a given expression in infix notation.
        Assuming full parenthesis with single space separation.
    """
    expr = parse_expression(expr)

    value_stack = Stack()
    operator_stack = Stack()

    i = 0

    while i < len(expr):

        # print('current token is {}'.format(expr[i]))
        if expr[i] == '(':
            operator_stack.push(expr[i])

        elif is_number(expr[i]):
            value_stack.push(int(expr[i]))

        elif is_operator(expr[i]):
            operator_stack.push(expr[i])

        elif expr[i] == ')':
            # pop two last numbers from the value stack
            value2 = value_stack.pop()
            value1 = value_stack.pop()

            # pop the operator
            operator = operator_stack.pop()

            # calculate the result for these two numbers
            # push the result onto the value stack again
            if operator == '+':
                value_stack.push(value1 + value2)

            elif operator == '-':
                value_stack.push(value1 - value2)

            elif operator == '*':
                value_stack.push(value1 * value2)

            elif operator == '/':
                try:
                    value_stack.push(value1 / value2)
                except ZeroDivisionError:
                    return "You can't divide by zero!"

            # pop the left parenthesis
            operator_stack.pop()

        # print('value_stack at the end of the step = {}'.format(value_stack.items))
        # print('operator_stack at the end of the step = {}'.format(operator_stack.items))
        # print('we went through all the options, incrementing i')

        # increment to the next element
        i += 1

    return value_stack.peek()


if __name__ == "__main__":
    print(evaluate_infix_notation("( 1 + 2 )"))  # expected 3
    print(evaluate_infix_notation("( 1 + ( 2 * 3 ) )"))  # expected 7
    print(evaluate_infix_notation("( ( 1 * 2 ) + 3 )"))  # expected 5
    print(evaluate_infix_notation("( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )"))  # expected -1.8
    print(evaluate_infix_notation("( 10 - ( 2 * 12 ) )"))  # expected -14
    print(evaluate_infix_notation("( ( 5 + 4 ) - ( 2 * 0 ) )"))  # expected 9
    print(evaluate_infix_notation("( 15 / ( 1 - 1 ) )"))  # expected division by zero













