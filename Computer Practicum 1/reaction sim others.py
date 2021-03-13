"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def rhs(y, t, kf, kb):
    rf = kf * y[0] * y[1]
    rb = kb * y[2]
    return [2*(rb - rf), rb - rf, 2*(rf - rb)]
tout = np.linspace(0, 10) #range of time
k_vals = 0.42, 0.17  # rate constant k1, k-1
y0 = [1, 1, 0] # initial molarity of A, B, C
yout = odeint(rhs, y0, tout, k_vals)
plt.plot(tout, yout)
_ = plt.legend(['A', 'B', 'C'])
plt.savefig('1.png')
plt.show()
"""
"""
from chempy import ReactionSystem
from chempy.kinetics.ode import get_odesys
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
# The rate constants below are arbitrary
rsys = ReactionSystem.from_string("""A + B -> C; 1
     C -> A + B; 0.5
     C -> D; 0.5""")
odesys, extra = get_odesys(rsys)
tout = sorted(np.concatenate((np.linspace(0, 23), np.logspace(-8, 1))))
c0 = defaultdict(float, {'A': 1, 'B': 1, 'C': 0.5, 'D': 0.5})
result = odesys.integrate(tout, c0, atol=1e-12, rtol=1e-14)
result.plot(names=[k for k in rsys.substances if k != 1])
plt.legend(loc='best', prop={'size': 9})
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.savefig('1.png')
plt.show()
"""

