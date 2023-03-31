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
One possible solution
'''
def formula(pairs):
    initial_constraint = sum([If(Bool(f'B{i}'), 1, 0) for i in range(4)]) == 1
    constraint = False
    for i in range(4):
        option_constraint = True
        for (x, y), ans in io_pairs:
            if i == 0:
                pair_constraint = mul(0, x,y) == ans
            if i == 1:
                pair_constraint = mul(1, y,x) == ans
            if i == 2:
                pair_constraint = shl(2, x,y) == ans
            if i == 3:
                pair_constraint = shl(3, y,x) == ans
            option_constraint = And(option_constraint, pair_constraint)
        constraint = Or(constraint, option_constraint)

    constraint = And(constraint, initial_constraint)
    return constraint

'''
Another possible solution
'''
def formula1(pairs):
    initial_constraint = sum([If(Bool(f'B{i}'), 1, 0) for i in range(4)]) == 1
    constraint = True
    for (x, y), ans in io_pairs:
        pair_constraint = mul(0,x,y) + mul(1,y,x) + shl(2,x,y) + shl(3,y,x) == ans
        constraint = And(constraint, pair_constraint)
    constraint = And(constraint, initial_constraint)
    return constraint

if __name__ == '__main__':
    s = formula(io_pairs)
    print(f'Z3 formula: {s}')
    print('Z3 Solution:')
    solve(s)
