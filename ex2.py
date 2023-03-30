from z3 import *
from itertools import *

io_pairs = [
   ((3, 5, 2),192),
   ((6, 9, 3),9216),
   ((23, 1, 1),46),  
   ((16, 6, 5),5120),  
   ((8, 9, 1),4096)
]

'''
Convenience functions for creating a constraint using a flag with identifier
'i' that toggles whether the operator is used for operands x1 and x2.
Use is OPTIONAL.
'''
def mul(i, x1, x2):
    return If(Bool(f'B{i}'), (x1 * x2), BitVecVal(0, 16))

def shl(i, x1, x2):
    return If(Bool(f'B{i}'), (x1 << x2), BitVecVal(0, 16))

'''
The main steps of the synthesis process are as follows:

1. Define Z3 variables and expressions for the possible operations.
2. Add a constraints to only allow one operation to be part of the solution per line.
3. Add constraints for each input-output pair.
4. Solve the Z3 formula to synthesize the function.
'''
def formula(pairs):

    constraint = True
    for inputs, output in io_pairs:
         
        # first op
        intermediate_result = BitVec(f"interm_{count}", 16)
     
        # second op
      
    return constraint

if __name__ == '__main__':
    s = formula(io_pairs)
    print(f'Z3 formula: {s}')
    print('Z3 Solution:')
    solve(s)
