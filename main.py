from __future__ import absolute_import
from pip._vendor.distlib.compat import raw_input
import argparse

from prefix import evaluate_prefix_notation
from infix import evaluate_infix_notation
from api.app import app


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Calculator processing prefix and infix notation')
    parser.add_argument('--mode', type=str, required=True, choices=('web-based', 'script'),
                        help='interact with the calculator over the web-based app vs a standalone script')
    parser.add_argument('--expression_type', type=str, choices=('prefix', 'infix'),
                        help='prefix or infix expression to be handled by script')

    args = parser.parse_args()

    if args.mode == 'script' and args.expression_type is None:
        parser.error("--script mode requires --expression_type to be scpecified")

    if args.mode == 'script' and args.expression_type == 'prefix':
        print("Enter expression in prefix notation, elements should be space separated:")
        expr = raw_input()
        print(evaluate_prefix_notation(expr))

    if args.mode == 'script' and args.expression_type == 'infix':
        print("Enter expression in infix notation, parenthesis, "
              "numbers and operators should be space separated:")
        expr = raw_input()
        print(evaluate_infix_notation(expr))

    if args.mode == 'web-based':
        app.run(debug=True, port=7089)
