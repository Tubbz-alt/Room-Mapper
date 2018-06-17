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
plt.plot(aX,bY)
plt.show()

