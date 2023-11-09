#Written b Jaise Johnson
#Date 03/8/2020

import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
def logistic(r,x):
    return r * x * (1 - x)
xlist = []
rlist = []
r = 1
while r < 4:
    x = 0.4
    for i in range(0,105):
        if i >= 100:
            xlist.append(x)
            rlist.append(r)
        x = logistic(r,x)
    r = r + 0.0001
plt.figure(figsize=(8,6),)
plt.plot(rlist, xlist, "k", ls = '', marker = ',')
plt.xlabel("Growth Rate")
plt.ylabel("Xn")
plt.title("Bifurcation Problem")
plt.legend(["x = 0.4,dr = 0.0001"])
plt.show()