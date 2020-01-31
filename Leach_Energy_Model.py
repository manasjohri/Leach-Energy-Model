import numpy as np
from math import *
import matplotlib.pyplot as plt
from sys import*
dx = []         
dy = []
df = []
fx = []
fy = []
hl = []
cn = []
s1 = []
lk = []
distance2 = []
e = 0.25
etx = float(format(50*(pow(10,-9)),'.200g'))
erx = float(format((50*(pow(10,-9))),'.200g'))
efs = float(format((100*(pow(10,-12))),'.200g'))
print(etx)
print(efs)
print(erx)
distance = []
for i in range(100):  
    m =  [np.random.randint(100), np.random.randint(100)]                           
    df.append(m)
for j in df:
    dx.append(j[0])                                                                    
    dy.append(j[1])                                                             
x = 100
y = 100
plt.title("Figure 1", color = 'red')
plt.xlabel('X- Axis', color = 'blue')
plt.ylabel("Y- Axis", color = 'blue')
plt.plot(100,100,'x',markersize=9,markeredgecolor = 'Black')
plt.plot(x,y,dx,dy,'o',markersize=8,markerfacecolor='white',markeredgecolor = 'Blue')
p = 0.05
count = 0
for i in range(100):
    rt1 = float(0.05)
    s1.append(rt1)
def points(n):
    dead=0
    for r in range(4000):
        for kl in range(100):
            if kl not in lk:
                if s1[kl]<=0:
                    lk.append(kl)
                    dead = dead+1
                    print("DEAD=>",dead)
                    plt.plot(dx[kl],dy[kl],'o',color = 'red') 
                    if dead == 1:
                        print("FND:- First Node Die Is At=>{}".format(r))
                    elif dead == 0.50*100:
                        print("HNA:- Half Node Alive Is At=>{}".format(r))
                    elif dead == 0.99*100:
                        print("LNA:- Last Node Alive Is At=>{}".format(r))
                    elif dead == 100:
                        print("ALL Dead At=>{}".format(r))
                        exit()
            if s1[kl]>0:
                temp_rand = np.random.randint(100)                          
                if(temp_rand <=  (p//(1-(p*(r%(round(1/p))))))):  
                    #if s1[kl]>0:
                        hl.append(kl)
                        s = (sqrt((pow((dx[kl]-x),2))+(pow((dy[kl]-y),2))))
                        distance.append(s)
                        s1[kl] = s1[kl]-(((etx*2000) + (((efs*2000)*(pow(s,2))))))
                        s = 0
        for i2 in range(100):
            if s1[i2]>0:
                if i2 not in hl:
                    for i1 in hl:
                        s2 = (sqrt((pow((dx[i2]-dx[i1]),2))+(pow((dy[i2]-dy[i1]),2))))
                        distance2.append(s2)
                        s2 = 0
                    if distance2!=[]:
                        s1[i2] = s1[i2] -(((etx*2000) + (((efs*2000)*(pow((min(distance2)),2))))))
                        for i3 in range(len(hl)):
                            if min(distance2)==distance2[i3]:
                                s1[hl[i3]] = s1[hl[i3]]-(erx*2000)
                        del distance2[:]
        yield hl
        del hl[:]
count1 = 0
for i in points(100):
    if i!=[]:
        print(i)

    for j in i:
            if j!=[]:
                count1 = count1+1
                count = count +1
                plt.plot(dx[j],dy[j],'o',markersize=4,color = 'black')
    plt.pause(0.3)
    if count1!=0:
        cn.append(count1)
        count1 = 0

    for j in i:
            if j!=[]:
                plt.plot(dx[j],dy[j],'o',markersize=4,color = 'white')
print(s1)
print(count)
plt.show()
