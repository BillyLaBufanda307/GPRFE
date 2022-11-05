import geopandas as gpd
import os
import matplotlib.pyplot as plt, numpy as np
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#x = np.arange(1,11) 
#y = 2 * x + 5 
#plt.title("Matplotlib demo") 
#plt.xlabel("x axis caption") 
#plt.ylabel("y axis caption") 
#plt.plot(x,y) 
#plt.show()

#v= np.array([[[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]]]) wrong fro some reason
v= np.array([[[1, 2, 3], [3, 4, 5]], [[5, 6, 7], [7, 8, 9]]])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(v[:,1],v[:,1],v[:,1])
plt.show()