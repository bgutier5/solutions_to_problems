import sympy
import pandas as pd
from sympy import nsimplify, sin, pi, integrate, exp, oo
sympy.init_printing()
from sympy.printing.latex import LatexPrinter, print_latex
from io import StringIO  # Python3
import sys



# Defining variables
 
r, t, p = sympy.symbols('r t p')
# where
# r = r coordinate
# t = theta
# p = phi
a = 1 # a = borh radius in atomic units 

# Defining functions

A = (27/(pi*a**3))**0.5
f = exp(-3*r/a)
Psi = A*f # non-stationary-state wavefunction

B = (1/pi)**0.5 * (1/a)**(3/2)
g = exp(-r/a)
psi = B*g # hydrogen eigenfunction for n=1

#energy_n = n**2*h**2/(8*m*l**2) # eigenvalue for a particle-in-box eigenfunction


# Integrating function or projecting coefficient

## Single step

integrad      = psi*Psi*r**2*sin(t)
coefficient_1 = integrate(integrad, (r, 0, oo ), (t, 0, pi), (p, 0, 2*pi))
probability_1 = coefficient_1**2
print('Probability (n=1) =', probability_1)

