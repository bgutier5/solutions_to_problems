import numpy as np
import matplotlib.pyplot as plt


R = 8.3145 

t_values = []
E_values = []
for t in range(12, 200):
	diff_temp = (1/(t + 10)) - (1/t)
	E_a = -R*np.log(2)/diff_temp
	t_values.append(t)
	E_values.append(E_a)

# Graphing data
plt.xlabel('temperature(K)')
plt.ylabel('energy barrier (J)')
plt.title('constante function?')
plt.plot(t_values, E_values, label='$E_a$')
plt.legend(bbox_to_anchor=(1, 1), loc='best', borderaxespad=0. )
plt.show()

 
