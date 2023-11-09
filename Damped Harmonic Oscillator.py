#Written by Jaise Johnson
#Date 24/06/2020

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
#initial condiions
x1 = 0
v1 = 1
a1 = 0
h = 0.1

x0 = -x1 - v1*h - (h**2*(v1 + x1))
print(x0)
'''
We have three cases of damped harmonic oscillators.
Underdamped Damped Harmonic Oscillators :  c < w
Critically Damped Harmonic Oscillators  : c = w
Overdamped Harmonic Oscillators         : c > w
'''


xio = x0
ai = a1
xi = x1
vi = v1

#iteration equations and iterations
print("position")
pos,velo,acc = [],[],[]
for i in range (0,500):
    xi1 = 2 * xi - xio - (vi + xi) * h ** 2  # xi1 = x(i+1), #xio = x(i-1)
    vi = (xi1 - xio)/2*h
    ai = (xi1 - 2*xi + xio)/ h**2
    pos.append(xi)
    velo.append(vi)
    acc.append(ai)
    xio = xi
    xi = xi1

fig,axs = plt.subplots(3,1,sharex=True)
axs[0].plot(pos)
axs[0].set_ylabel('Position')

axs[1].plot(velo)
axs[1].set_ylabel('Velocity')

axs[2].plot(acc)
axs[2].set_ylabel('Acceleration')
plt.show()

plt.plot(pos,velo)
plt.title('Phase Space Plot')
plt.xlabel('Position')
plt.ylabel('Velocity')
plt.show()