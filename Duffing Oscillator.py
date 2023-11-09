'''
Written by Jaise Johnson
Date : 19/9/2020
A non - linear oscillator with the force equation
ma = -kv + 2ax - 4bx^3 + Focos(wt) is called as a duffing oscillator.
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

xi = 0.5
vi = 2
ai = 0
h = 0.1
k = 0.1
b = 0.1
f0 = 2
a = 0.5
w = 0.1
t = 0

xio = (-2*vi*h + h**2*(- xi*k + 2*a*xi -4*b*xi**3 + f0*np.cos(w*t)) + 2*xi)/2
print(w)


'''
For iterating 
'''
pos,velo = [],[]
for i in range(600):
    xi1 = h**2*(-xi*k + 2*a*xi - 4*b*xi**3 +f0*np.cos(w*t) ) + 2*xi - xio
    vi = (xi1- xio)/2*h
    pos.append(xi)
    velo.append(vi)
    #print(xio)
    xio = xi
    xi = xi1
    t = t + h
    #print(xi1)

fig,axs = plt.subplots(2,1,sharex=True)
axs[0].plot(pos)
axs[0].set_ylabel('Position')

axs[1].plot(velo)
axs[1].set_ylabel('Velocity')
plt.show()



plt.plot(pos,velo)
plt.title('Phase Space Plot')
plt.xlabel('Position')
plt.ylabel('Velocity')
plt.show()


