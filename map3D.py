
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

aX=[]
bY=[]
file=open('rmx/x.txt',"r")
for i in file:
	i=i.strip()
	if(i!='' and i!='null'):
		aX.append(int(i))
file.close()
file=open("rmy/y.txt","r")
for i in file:
	i=i.strip()
	if(i!='' and i!='null'):
		bY.append(int(i))
file.close()

X = aX
Y = bY
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)

plt.show()

