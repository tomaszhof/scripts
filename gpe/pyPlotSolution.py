import sys
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter, ScalarFormatter
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def plotResults(a1, a2, b1, b2, fname, ofname):
  #read data from csv file
  print('Reading data from csv file...')
  a = np.genfromtxt(fname, delimiter=';')
  noRows = a.shape[0]
  noCols = a.shape[1]
  a = a[0:noRows, 0:(noCols-1)]
  deltaX = a2-a1
  deltaY = b2-b1
  stepX = deltaX / (noRows)
  stepY = deltaY / (noCols-1)
  print('done.')

  print('Preparing plot...')
  fig = plt.figure(figsize=(5, 3), dpi=500)
  ax = fig.gca(projection='3d')
  X = np.arange(a1, a2, stepX)
  Y = np.arange(b1, b2, stepY)
  X, Y = np.meshgrid(X, Y)
  Z = a
  vMax=Z.max()
  vMin=Z.min()
  vMax=vMax+0.1*abs(vMax)
  vMin=vMin-0.1*abs(vMin)
  surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.Greys_r,
        linewidth=0, antialiased=True, vmin=vMin, vmax=vMax)
  zAxisFormatter = ScalarFormatter()
  zAxisFormatter.set_scientific(True)
  zAxisFormatter.set_powerlimits((0, 1))
  #ax.zaxis.set_major_formatter(zAxisFormatter)
  print('Drawing...')
  fontSize=8 #set fontsize on plot
  ax.set_xlabel('x', fontsize=fontSize)
  ax.set_ylabel('y', fontsize=fontSize)
  ax.zaxis.set_rotate_label(False)
  ax.set_zlabel('u(x,y)', fontsize=fontSize, rotation=90)
  ax.view_init(27, 35)
  t = ax.zaxis.get_offset_text()
  t.set_size(fontSize-2)
  #t.set_position((0,0))
  t.set_rotation(45)
  t.set_verticalalignment('center')
  #t.set_z(0)
  plt.setp(ax.get_xticklabels(), fontsize=fontSize)
  plt.setp(ax.get_yticklabels(), fontsize=fontSize)
  plt.setp(ax.get_zticklabels(), fontsize=fontSize)
  plt.legend()
  cbar=fig.colorbar(surf, shrink=0.75, aspect=15)
  cbar.ax.tick_params(labelsize=fontSize)
  
  #plt.show()
  plt.savefig(filename=ofname, format='eps')
  plt.close()

def main():
  alpha1 = float(sys.argv[1])
  alpha2 = float(sys.argv[2])
  beta1 = float(sys.argv[3])
  beta2 = float(sys.argv[4])
  fname = str(sys.argv[5])
  ofname = str(sys.argv[6])
  plotResults(alpha1, alpha2, beta1, beta2, fname, ofname)

if __name__=="__main__":main()
