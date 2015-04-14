#!/usr/bin/env python
import sys
import numpy as np
import pylab as P
from matplotlib.ticker import LinearLocator, FormatStrFormatter, ScalarFormatter
from numpy import genfromtxt
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def plot_hist(fnames):
  fontSize=3
  fig, ax = plt.subplots(2, 2, figsize=(5, 3), dpi=500)
  plt.xlim(0.0, 1.0)
  k = 0
  for i in range(2):
  	for j in range(2):
  		sub1 = ax[i][j]
  		sub1.set_xlim(0.0, 1.0)
  		fname = fnames[k]
  		k = k + 1
  		M = genfromtxt(fname, delimiter=';')
  		M=M[:,:-1]
  		A = np.asarray(M).reshape(-1)
  		n, bins, patches = sub1.hist(A, 20, fc='gray', weights=np.zeros_like(A) + 1. / A.size)
  		plt.setp(sub1.get_xticklabels(), fontsize=fontSize)
  		plt.setp(sub1.get_yticklabels(), fontsize=fontSize)
  		sub1.set_xlabel('Relative position of the solution in the interval', fontsize=fontSize)
  		sub1.set_ylabel('Probability', fontsize=fontSize)
  fig.tight_layout()
  plt.show()


def main():
  f1name = str(sys.argv[1])
  f2name = str(sys.argv[2])
  f3name = str(sys.argv[3])
  f4name = str(sys.argv[4])
  fnames = [f1name, f2name, f3name, f4name]
  plot_hist(fnames)

if __name__=="__main__":main()
