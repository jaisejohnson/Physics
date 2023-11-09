#Written by Jaise Johnson
#Date 21/6/2020

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use('ggplot')
plt.figure(figsize=(8,8))


'''We have defined trapezoidal rule here.
We multiply throughout the list with h/2 and all values of the list except the first and the last are
multiplied by 2'''
def trapezoidal(h,xlist):
    area = 0
    for i in range (0,len(xlist)):
        if i == 0 or i == len(xlist):
            a = (h / 2) * xlist[i]
        else:
            a = (h/2)*xlist[i]*2
        area = area + a
    return(area)

'''Im order to normalise a wave function we need to find the normalization constant and divide through out.
We know that that we have to multiply the state function with it's hermitian. Here we take the square'''
def pdf(xlist):
    xsql = []
    for x in xlist:
        xsq = (x**2)
        xsql.append(xsq)
    return (xsql)


'''After applying the trapezoidal rule on the pdf of the wavefunction now we get,the area bounded by the curve.
To obtain the normalization we take the square root of the quantity and divide the wavefunction with it, to obtain
 the normalised wavefunction'''
def normalisation (xlist):
    rzl = []
    for x in xlist:
        ele = x/(np.sqrt(trapezoidal(h,pdf(xlist))))
        rzl.append(ele)
    return(rzl)

n = 5
Elist = []
norm = []
unnorm = []
while n <= 400:
    xi = 0
    h = 0.01
    vi = 1
    ai = 0
    m,L,hcross = 1,1,1
    E = n
    k = 2*m*E/hcross**2
    xio = -(-k * xi * h ** 2 + 2 * xi + 2 * h * vi) / 2
    xlist = []
    vlist = []
    for i in range(0,100):
        xi1 = 2 * xi - xio - (k * xi * h**2)
        vi = (xi1 - xio)/2*h
        xlist.append(xi)
        vlist.append(vi)
        xio = xi
        xi = xi1

    if (round(abs(vlist[-1])/abs(max(vlist)),3))== 1:
        unnorm.append((np.sqrt(trapezoidal(h,pdf(xlist)))))            #this is unnormalised, areas shoiudn't be equal to 1
        norm.append(np.sqrt(trapezoidal(h,pdf(normalisation(xlist))))) #this is the normalised area,if this is equal to 1 our wnfs are normalised
        Elist.append(E)
        print("xlist = " + str(xlist))
        newlist = normalisation(xlist)
        print("normalised xlist = " + str(newlist))
        #print(trapezoidal(h,pdf(normalisation(xlist))))
        #plt.title("Unnormalised")
        #plt.ylabel("Psi(x)")
        #plt.plot(((xlist)))
        #plt.grid()
        #plt.subplot(212)

    plt.plot(newlist, color = 'DarkBlue')
    plt.xlabel("x")
    plt.legend(Elist)
    plt.xticks([0,25,50,75,100],["0","0.25","0.5","0.75","1"])
    plt.yticks(np.arange(0,2,step = 0.25))
    plt.title("Particle in a Box")
    plt.ylabel("Psi(x)")


    n = n + 1
#print(unnorm)
#print(norm)
plt.show()
