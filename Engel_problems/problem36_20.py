
import numpy as np
import matplotlib.pyplot as plt

A_0 = 1 # Molar
B_0 = 0
C_0 = 0
factor = 1
k_A = 1e-3 #s^-1
k_B = factor*k_A
t_0 = 0
t_step = 0.5 # sec
t_total = 1000
n_steps = int(t_total/t_step)

t_values = []
A_concentrations = []
B_concentrations = []
C_concentrations = []
for step in range(n_steps):
	A_1 = -k_A*A_0*t_step + A_0
	B_1 = (k_A*A_0 - k_B*B_0)*t_step + B_0
	C_1 = k_B*B_0*t_step + C_0 
	t_values.append(t_0)
	A_concentrations.append(A_1)	
	B_concentrations.append(B_1)	
	C_concentrations.append(C_1)
	A_0 = A_1
	B_0 = B_1
	C_0 = C_1
	t_0 = t_0 + t_step

#print(np.array(C_concentrations))

# Graphing data
plt.xlabel('time(secs)')
plt.ylabel('Concentration(M)')
plt.title('Species evolution when $k_A = k_B$')
plt.plot(t_values, A_concentrations, label='[A]')
plt.plot(t_values, B_concentrations, label='[B]')
plt.plot(t_values, C_concentrations, label='[C]')
plt.legend(bbox_to_anchor=(1, 1), loc='best', borderaxespad=0. )
plt.show()

