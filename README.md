# Inductive Program Synthesis

Programming by Example (PBE) is the process of generating a program from a set of input-output pairs (or examples). In PBE, the goal is learn a program that can generalize from the given examples and produce correct outputs for inputs not seen before.

In this recitation, you are going to synthesize a simple function using Z3, an SMT (Satisfiability Modulo Theories) solver. 
Given a set of input-output pairs, your goal is to construct a Z3 formula that represents the constraints imposed by these examples. The Z3 solver will then attempt to find a solution that satisfies all of the constraints, effectively synthesizing the function that corresponds to the input-output pairs.

To accomplish this, you will need to create Z3 variables and expressions that represent the possible operations, and use them to construct constraints based on the input-output pairs. The mul and shl convenience functions provided in the problem.py template can be used to create such constraints.


### Set up

Set up the Python interface for Z3 using `pip install z3-solver` or use Codespaces


### Function Specification:

The function will take two ORDERED inputs, and produces an output. Based on magic intuition, we know the following about the function:
1. It only uses the operations * and <<
2. It returns the result of a single statement of the form
    [Input_x] [op] [Input_y]
3. It uses both inputs, but you do not know in what order.

### Function IO Pairs:
   IN: (3, 5)    OUT: 40  
   IN: (6, 9)    OUT: 576  
   IN: (23, 44)  OUT: 369098752  
   IN: (16, 22)  OUT: 1441792  
   IN: (8, 9)    OUT: 2304  

From the given IO pairs, you may already be able to tell what the function should be,
but we can still formulate this as a synthesis problem and use Z3 to solve it. This technique
will become especially helpful for dealing with more complicated functions (i.e. like the one you will synthesize in HW8). 

You can use the template in `problem.py` to help you get started!


The main steps of the synthesis process are as follows:

- Define Z3 variables and expressions for the possible operations.
- Add a constraints to only allow one operation to be part of the solution.
- Add constraints for each input-output pair.
- Solve the Z3 formula to synthesize the function.


```python
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
```
# Resources

- [Python Z3 examples](http://ericpony.github.io/z3py-tutorial/guide-examples.htm)
- [Python API](http://z3prover.github.io/api/html/namespacez3py.html)
- [Programming Z3, a guide](http://theory.stanford.edu/~nikolaj/programmingz3.html)
