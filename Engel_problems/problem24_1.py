H_11 = -13.6  #eV
H_22 = -13.6

def energy(S, H_22, H_11):
    H_12 = round( -1.75*S*abs(H_22), 1)
    a    = H_11 + H_22 -2*S*H_12
    P    = 1/( 2-2*(S**2) )
    b    = (H_11**2 + 4*H_12**2 + H_22**2 - 4*S*H_12*H_22 - 2*H_11*(H_22 + 2*S*H_12 - 2*S**2*H_22) )**0.5
    e1   = round( P*a + P*b, 1)
    e2   = round( P*a - P*b, 1)
    return(H_12, e1, e2)

def energy2(S, H_22, H_11):                 # The formula simplyfies to this when the two atoms are the same (homonuclear)
    H_12 = round( -1.75*S*abs(H_22)  , 1 )
    e1   = round( (H_11 + H_12)/(1+S), 1 )
    e2   = round( (H_11 - H_12)/(1-S), 1 )
    return(H_12, e1, e2)
 

separation = [0.1, 0.2, 0.6]
for S in separation:
    H, plus_e, minus_e = energy(S, H_22, H_11)
    #H, plus_e, minus_e = energy2(S, H_22, H_11)
    print('S = {:>5} H_12 = {:>5} plus_e = {:>5} minus_e = {:>5}'.format(S, H, plus_e, minus_e) ) 
