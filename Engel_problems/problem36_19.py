
import numpy as np
import matplotlib.pyplot as plt

A_0 = 1 # Molar
B_0 = 0
C_0 = 0
factor = 1
k_A = 1e-3 #s^-1
k_B = factor*k_A
t = 0
t_step = 0.5 # sec
t_total = 1000
n_steps = int(t_total/t_step)

t_values = [t]
A_concentrations = [A_0]
B_concentrations = [B_0]
C_concentrations = [C_0]
for step in range(n_steps):
	A = A_0*np.exp(-k_A*t)
	B = (k_A/(k_B-k_A))*A_0*(np.exp(-k_A*t) - np.exp(-k_B*t)	)
	ratio_exp = (k_A*np.exp(-k_B*t) - k_B*np.exp(-k_A*t))  / (k_B - k_A)
	C = A_0*( ratio_exp + 1 )
	t_values.append(t)
	A_concentrations.append(A)	
	B_concentrations.append(B)	
	C_concentrations.append(C)
	#A = A_1
	#B = B_1
	#C = C_1
	t = t + t_step

#print(np.array(C_concentrations))

# Graphing data
plt.xlabel('time(secs)')
plt.ylabel('Concentration(M)')
plt.title('Species evolution')
plt.plot(t_values, A_concentrations, label='[A]')
plt.plot(t_values, B_concentrations, label='[B]')
plt.plot(t_values, C_concentrations, label='[C]')
plt.legend(bbox_to_anchor=(1, 1), loc='best', borderaxespad=0. )
plt.show()

