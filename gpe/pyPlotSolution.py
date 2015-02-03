import sys
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

def plotResults(a1, a2, b1, b2, fname):
  print('P0')
  a = np.genfromtxt(fname, delimiter=';')
  noRows = a.shape[0]
  noCols = a.shape[1]
  print('P1')
  a = a[0:noRows, 0:(noCols-1)]
  deltaX = a2-a1
  deltaY = b2-b1
  stepX = deltaX / (noRows)
  stepY = deltaY / (noCols-1)
  fig = plt.figure(figsize=(14, 8), dpi=80)
  print('P2')
  ax = fig.gca(projection='3d')
  X = np.arange(a1, a2, stepX)
  Y = np.arange(b1, b2, stepY)
  X, Y = np.meshgrid(X, Y)
  Z = a
  #cmap=cm.coolwarm
  vMax=Z.max()
  vMin=Z.min()
  vMax=vMax+0.1*abs(vMax)
  vMin=vMin-0.1*abs(vMin)
  surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.Greys_r,
        linewidth=0, antialiased=False, vmin=vMin, vmax=vMax)
  #ax.set_zlim(-1.01, 1.01)
  ax.zaxis.set_major_locator(LinearLocator(10))
  ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
  fig.colorbar(surf, shrink=0.5, aspect=15)
  print('Drawing...')
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_zlabel('u(x,y)')
  ax.view_init(27, 35)
  #plt.show()
  plt.savefig(filename='plot.eps', format='eps')
  plt.close()

def main():
  alpha1 = float(sys.argv[1])
  alpha2 = float(sys.argv[2])
  beta1 = float(sys.argv[3])
  beta2 = float(sys.argv[4])
  fname = sys.argv[5]
  plotResults(alpha1, alpha2, beta1, beta2, fname)

if __name__=="__main__":main()
