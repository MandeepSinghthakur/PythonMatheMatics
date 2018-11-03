# The Derivative  of a function y = f(x) expresses the rate of change in the dependent variable
# y with respect to the independent variable , x. It's denoted as either f'x or dy/dx.


#Derivative Calculator
from sympy import Symbol, Derivative, sympify, pprint
from sympy.core.sympify import SympifyError

def derivative(f, var):
    var = Symbol(var)
    d = Derivative(f,var).doit()
    pprint(d)

if __name__ == '__main__':
    f = input('Enter a function: ')
    var = input('Enter the variable to diffrentiate with respect to: ')
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid input')
    else:
        derivative(f, var)