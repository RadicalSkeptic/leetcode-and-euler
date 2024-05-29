import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.optimize import fsolve

x,y=1.4,-9.6
n=0
xx=[]
yy=[]
m1=-197/14
while y<0 or not -.01<x<.01:
    m=-4*x/y
    m2=math.tan(2*math.atan(m)-math.atan(m1))
    c=y-m2*x

    # xp=(-m2*c+math.sqrt(m2**2*c**2-(4+m2**2)*(c**2-100)))/(4+m2**2)
    # yp=m2*xp+c
    # xn=(-m2*c-math.sqrt(m2**2*c**2-(4+m2**2)*(c**2-100)))/(4+m2**2)
    # yn=m2*xn+c
    # if (abs(x-xp)+abs(y-yp)) > (abs(x-xn)+abs(y-yn)):
    #     x,y=xp,yp
    # else:x,y=xn,yn

    x=-2*m2*c/(4+m2**2)-x #Damn i overcomplicated this
    y=m2*x+c
    
    m1=m2
    n+=1
    xx.append(x)
    yy.append(y)

print(n)

fig = plt.figure()
plt.xlim(-10, 10)
plt.ylim(-10, 10)
graph, = plt.plot([], [])
def animate(i):
    graph.set_data(xx[:i+1], yy[:i+1])
    return graph
ani = FuncAnimation(fig, animate, frames=len(xx)+100, interval=20)
plt.show()