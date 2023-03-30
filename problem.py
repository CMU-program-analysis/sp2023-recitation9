from z3 import *

io_pairs = [
    ((3, 5), 40),
    ((6, 9), 576),
    ((23, 44), 369098752),
    ((16, 22), 1441792),
    ((8, 9), 2304),
]

'''
Convenience functions for creating a constraint using a flag with identifier
'i' that toggles whether the operator is used for operands x1 and x2.
Use is OPTIONAL.
'''
def mul(i, x1, x2):
    return If(Bool(f'B{i}'), (x1 * x2), 0)

def shl(i, x1, x2):
    return If(Bool(f'B{i}'), (x1 << x2), 0)

'''
Your Synthesizer: construct a Z3 formula using input/output pairs.
Hints:
    1. Consider encoding each possible function using Z3 Bool variables 
    2. Add a constraint that only allows one operation to be a part of the solution
    2. Add a constraint/constraints for each IO pair
'''
def formula(pairs):
    constraint = True
    for (x, y), ans in io_pairs:
        constraint = True
    return constraint

if __name__ == '__main__':
    s = formula(io_pairs)
    print(f'Z3 formula: {s}')
    print('Z3 Solution:')
    solve(s)
