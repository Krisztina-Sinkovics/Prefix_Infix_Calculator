This is a repository hosting a simple calculator that can handle prefix and infix expressions.

### Requirements:
python version: 3.7  
testing: pytest

### Assumptions:
- All the tokens are space-separated, including the parenethesis tokens for infix notation
- The system should support the operators {+, -, *, /} which all take exactly two args.
- The input literals are positive integers
- Calculations can be done in the floating-point or integer domain
- In case of prefix notation operator precedence is handled by the specifics of the notation 
- In case of infix notation operator precedence is handled by the parenthesis
