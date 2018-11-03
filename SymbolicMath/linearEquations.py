from sympy import solve, Symbol , pprint

x = Symbol('x')
y = Symbol('y')

expr1 = 2*x + 3*y - 6
expr2 = 3*x + 2*y - 2

print(solve((expr1, expr2), dict=True))