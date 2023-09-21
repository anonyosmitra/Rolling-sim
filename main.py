import math
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
g=10
h=20
r=2
m=1
dt=.05
a=math.radians(45)
isl=ihw=None
def roll(ib):
    global g,h,r,n,a,isl,ihw
    db=dw=beta=dv=dx=w=x=v=0
    y=r
    t=0
    acc=g*math.sin(a)/(1+ib/(m*math.pow(r,2)))
    y1s=[]
    x1s=[]
    y2s=[]
    x2s=[]
    tab=[]
    y4=1
    started=False
    while y4>=0:
        x += dx
        v += dv
        if not started:
            v2 =v+acc*dt/2
            dx=v2*dt
            started=True
        else:
            dx=v*dt
        dv=acc*dt
        x3=x*math.cos(-a)-y*math.sin(-a)
        y4=x*math.sin(-a)+y*math.cos(-a)+h
        e=r
        w+=dw
        w2=w+e*dt/2
        beta+=db
        db=w2*dt
        dw=e*dt
        x1=r*math.sin(beta)+x3
        y1=r*math.cos(beta)+y4
        y1s.append(y1)
        x1s.append(x1)
        y2s.append(y4)
        x2s.append(x3)
        tab.append([t,x,y,v,acc,dx,dv,x3,y4,beta,w,e,x1,y1])
        t+=dt
    print(tabulate(tab,headers=["t","x","y","v","acc","dx","dv","x2","y2","beta","w","e","x1","y1"]))
    plt.plot(np.array(x1s),np.array(y1s))
    plt.scatter(np.array(x2s), np.array(y2s))
    plt.plot(np.array([0,h]), np.array([h,0]))
    plt.show()






        


def start():
    global isl,ihw,r
    isl =2/5*m*math.pow(r,2)
    ihw =2/3*m*math.pow(r,2)
    roll(isl)
start()