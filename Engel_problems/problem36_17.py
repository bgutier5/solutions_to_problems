import numpy as np
import matplotlib.pyplot as plt

# This script calculates and graphs the concentrations over time
# of the next chemical system
#  
#  A --k_1--> B
#  A --k_2--> C --k_3--> D
#

# Inital concentrations and parameters
A_0 = 1 # Molar
B_0 = 0 #  ""
C_0 = 0 #  ""
D_0 = 0 #  ""
k_1 = 1.5e-3 # sec^-1
k_2 = 2.5e-3 # ""
k_3 = 1.8e-3 # ""
t_0 = 0        # secs
t_step = 0.2   #  "" 
t_total = 1000 #  ""


# Calculation of concentrations over time
total_steps = int(t_total/t_step)
t_values = []
A_concentrations = []
B_concentrations = []
C_concentrations = []
D_concentrations = []
for t in range(total_steps):
	t_values.append(t_0)
	A_concentrations.append(A_0)
	B_concentrations.append(B_0)
	C_concentrations.append(C_0)
	D_concentrations.append(D_0)
        # DON'T REORDER to A,B,C,D!! or the concentrations will not update correctly in each iteration
	D_0 = k_3*C_0*t_step + D_0  
	B_0 = k_1*A_0*t_step + B_0
	C_0 = (k_2*A_0 - k_3*C_0)*t_step + C_0
	A_0 = -(k_1 + k_2)*A_0*t_step + A_0
	t_0 = t_0 + t_step


# Graphing data
plt.xlabel('time(secs)')
plt.ylabel('Concentration(M)')
plt.title('Species evolution')
plt.plot(t_values, A_concentrations, label='[A]')
plt.plot(t_values, B_concentrations, label='[B]')
plt.plot(t_values, C_concentrations, label='[C]')
plt.plot(t_values, D_concentrations, label='[D]')
plt.legend(bbox_to_anchor=(1, 1), loc='best', borderaxespad=0. )
plt.show()

 
