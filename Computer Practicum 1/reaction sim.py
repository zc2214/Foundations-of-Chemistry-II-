import matplotlib.pyplot as plt 
#def rate constant k and initial concentration
k1f = 10
k1r = 5
k2 = 5
A = 2
B = 1
C = 0.5
D = 0
#def time slot
time = 0
time_slot = 1e-3
#Mark the first points
plt.scatter(time, A, c = "blue")
plt.scatter(time, B, c = "red")
plt.scatter(time, C, c = "yellow")
plt.scatter(time, D, c = "green")
#Begin compute and mark the following points
loop = True
while loop:
    time = time + time_slot
    print("current reaction time:", time)
    # compute slope
    slopeA = -k1f * A
    slopeB = -k1f * B
    slopeC = -k1r * C - k2 * C
    slopeD = k2 * C
    # compute concentration
    A = A + slopeA * time_slot
    B = B + slopeB * time_slot
    C = C + slopeC * time_slot
    D = D + slopeD * time_slot
    # mark points
    plt.scatter(time, A, c = "blue")
    plt.scatter(time, B, c = "red")
    plt.scatter(time, C, c = "yellow")
    plt.scatter(time, D, c = "green")
    # test if reaches convergence
    if slopeA >= 1e-2 or slopeA<= -1e-2:
        loop  =True
    else:
        loop = False
#fig info
plt.legend(['A', 'B', 'C', 'D'])
plt.ylabel("concentration (mol/L)")
plt.xlabel("time (s)")
plt.savefig('reaction sim.png')
plt.show()
