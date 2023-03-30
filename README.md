# Set up

Set up the Python interface for Z3 using `pip install z3-solver`

# Challenge

Synthesize a simple function using Z3!

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
