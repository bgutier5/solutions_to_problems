import numpy as np
# this script calculates the rate constant of first order
# if this data set corresponds to a first order reaction
# the rate constant should be equal for every point.


time   = [0, 3, 6, 9, 12, 15]
P_total= [11.07, 14.79, 17.26, 18.90, 19.99, 20.71]

def P_A(P_total):
	P_0 = 11.07
	return 2*P_0-P_total 

PA_list = []
n_pressures =  len(P_total)
for i in range(n_pressures-1):
	PA1 = P_A(P_total[i])
	PA2 = P_A(P_total[i+1])
	rate_constant = (np.log(PA2) - np.log(PA1) )/(time[i] - time[i+1])
	print('K=', rate_constant)
	#PA_list.append(PA2)

for i in range(n_pressures):
	P_i = P_A(P_total[i])
	ln_Pi = np.log(P_i)
	PA_list.append( ln_Pi )
m, b = np.polyfit(time, PA_list, 1)

print('m=', m, 'b=', b)
