from sympy import solve, Symbol , pprint
x = Symbol('x')
expr = pow(x,2) + 5*x +4
print(solve(expr, dict =True))

## Lets Solve one more Equation
# According to one of the equations of motion, the distance travelled by body moving with a constant 
# acceleration a, with an initial velocity u, in time t is given by
# s = ut + at^2 /2

s = Symbol('s')
u = Symbol('u')
t = Symbol('t')
a = Symbol('a')

expr = u*t + (1/2)*a*t*t -s 
t_expr = solve(expr,t,dict=True)
pprint(t_expr)