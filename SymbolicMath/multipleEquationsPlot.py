# You can enter multiple expressions when calling the SymPy plot
# function to plot more than one expression on the same graph. For Example
# the following code plots two lines at once

from sympy.plotting import plot
from sympy import Symbol

x = Symbol('x')
plot(2*x+3,3*x+1)