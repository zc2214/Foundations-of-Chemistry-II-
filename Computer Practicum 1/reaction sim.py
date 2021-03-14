import matplotlib.pyplot as plt 
#def rate constant k and initial concentration
k1f = 100
k1r = 10
k2 = 50
A = 2
B = 1
C = 0
D = 0
#def time slot
time = 0
time_slot = 1e-3
#Crate lists
A_list = [A]
B_list = [B]
C_list = [C]
D_list = [D]
time_list = [time]
#Begin compute and mark the following points
loop = True
while loop:
    time = time + time_slot
    print("current reaction time:", time)
    # compute slope
    slopeA = -k1f * A * B + k1r * C
    slopeB = -k1f * A * B + k1r * C
    slopeC = k1f * A * B -k1r * C - k2 * C
    slopeD = k2 * C
    # compute concentration
    A = A + slopeA * time_slot
    B = B + slopeB * time_slot
    C = C + slopeC * time_slot
    D = D + slopeD * time_slot
    # add to lists
    A_list += [A]
    B_list += [B]
    C_list += [C]
    D_list += [D]
    time_list += [time]
    # test if reaches convergence
    if slopeA >= 1e-2 or slopeA<= -1e-2:
        loop  =True
    else:
        loop = False
#fig info
plt.plot(time_list, A_list, label = "A")
plt.plot(time_list, B_list, label = "B")
plt.plot(time_list, C_list, label = "C")
plt.plot(time_list, D_list, label = "D")
plt.legend(['A', 'B', 'C', 'D'])
plt.ylabel("concentration (mol/L)")
plt.xlabel("time (s)")
plt.savefig('reaction sim.png')
plt.show()
