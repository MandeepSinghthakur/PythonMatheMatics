# Sometimes we're just interested in finding the global maximum for a function instead of all local and global
# maxima or minima. For example, we might want to discover the angle of projection for which 
# a ball will cover the maximum horizontal distance. We're going to learn a new , more practical
# approach to solve such a problem. This approach makes use of the first derivative only, so its applicable 
# only to functions for which the first derivative can be calculated

# This method is called the GRADIENT ASCENT METHOD, which is iterative approach to finding the 
# global maximum. Because the gradient ascent method involves lots of computation, it's perfect kind of thing to solve
# programmatically rather than by hand. 

# A generic program for Gradient Ascent

from sympy import Derivative, Symbol, sympify

def grad_ascent(x0, f1x, x):
    epsilon = 1e-6
    step_size = 1e-4
    x_old = x0
    x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
    while abs(x_old - x_new) > epsilon:
        x_old = x_new
        x_new = x_old + step_size*f1x.subs({x:x_old}).evalf()
    return x_new

if __name__ == '__main__':
    f = input('Enter a function in one variable: ')
    var = input('Enter the variable to diffrentiate with respect to: ')
    var0 = float(input('Enter the initial value of the variable: '))
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid function entered')
    else:
        var = Symbol(var)
        d = Derivative(f,var).doit()
        var_max = grad_ascent(var0, d, var)
        print('{0}: {1}'.format(var.name, var_max))
        print('Maximum value: {0}'.format(f.subs({var:var_max})))