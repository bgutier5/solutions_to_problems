import sympy
from sympy import nsimplify, sin, pi, integrate

# Description
# This file computes the possible energy eigenvalues  and the correspoding probabilities for the problem 37.7 of the Levine, Quantum Chemistry, 7th
# The system is a particle in a box with the non-stationary wavefunction  
#
#  Psi = (105/l**7)**0.5*x*2*(l-x)
# \Psi =  (\frac{105}{l^7})^{\frac{1}{2}} x^2(l-x)     <-- latex notation
#
# A more detailed explanation of this procedure is in my notebook (black cover/brand: mead) for Levine solutions

# Quantum numbers (n) to compute
n_values = [1,2,3] 



# Defining variables 
x, n, l, m, h = sympy.symbols('x n l m h') 
# where
# l = length of box
# n = energy quantum number
# x = x coordinate
# m = particle mass
# h = planck constant



# Defining functions
A = (105/l**7)**0.5
f = x**2*(l-x)
Psi = A*f # non-stationary-state wavefunction

B = (2/l)**0.5
g = sin(n*pi*x/l)
psi = B*g # particle-in-box eigenfunction

energy_n = n**2*h**2/(8*m*l**2) # eigenvalue for a particle-in-box eigenfunction



# Integrating function or projecting coefficient
integrad = psi*Psi
coefficient_n = integrate(integrad, (x, 0, l))
probability_n = coefficient_n**2



# Printing values table
print('-------------------------------------------------------')
print('| {} | {:^20} | {:^25} |  '.format( 'n', 'Energy' , 'Probability') )
print('-------------------------------------------------------')
for n_i in n_values:
    energy_ni_value = energy_n.subs(n, n_i)                       # evaluating function with value n_i
    probability_ni_value = nsimplify(probability_n.subs(n, n_i))  # using nsimplify b/c sympy is not smart enough to simplify powers of l(length)
    prob_analytical_form = str(probability_ni_value)              # you need to transform the output of sympy to string, otherwise get an error in format function 
    prob_numerical_value = float((probability_ni_value).evalf())  # evaluation numerically the analytical expresion. Tranform to float, otherwise get an error in format function
    print('| {} | {:>20} | {:>15} = {:.5f} |  '.format( n_i, str(energy_ni_value), prob_analytical_form, prob_numerical_value) )   
print('-------------------------------------------------------')


