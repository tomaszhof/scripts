import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from collections import defaultdict, OrderedDict
from itertools import cycle
import sys


class ResultsContainer:
   """class for results storage"""
   
   def __init__(self):
     self.innerDict=dict()
     self.labelEl1="m=n"
     self.labelEl2="value"
     self.fontSize=12
     self.outputFileName='test.eps'
     self.line1Title="const_M"
     self.line2Title="const_M_exact"
     self.yMin=None
     self.yMax=None

   def setYLimits(self, YMin, YMax):
     self.yMin=YMin
     self.yMax=YMax
   
   def setLinesTitles(self, l1t, l2t):
     self.line1Title=l1t
     self.line2Title=l2t

   def setLabels(self, lEl1, lEl2):
     self.labelEl1=lEl1
     self.labelEl2=lEl2
   
   def setFontSize(self, fs):
     self.fontSize=fs
   
   def setOutputFileName(self, ofn):
     self.outputFileName=ofn

   def gatherResults(self, fname, arthId):
     a = np.genfromtxt(fname, delimiter=';')
     noRows = a.shape[0]
     print(a.shape)
     
     dx = []
     dy = []
     for i in range(noRows):
       dataTuple=tuple(a[i])
       (m, x, y, l, r, w) = dataTuple
       dx.append(m)
       dy.append(w)
     l=(dx, dy)
     print('Adding ' + str(arthId))
     self.innerDict[arthId]=l
     print(self.innerDict)

   def visualizeResults(self):
     f, ax = plt.subplots(figsize=(4, 4), dpi=300)
     linestyle = '--'
     color = 'cornflowerblue'
     text_style = dict(horizontalalignment='right', verticalalignment='center',
		      fontsize=12, fontdict={'family': 'monospace'})

     i=1
     noItems=len(self.innerDict)
     lines = ["o-","o--","o-.","o:"]
     linecycler = cycle(lines)
     noStyles=len(lines)
     lArr=[]
     i=0
     print(self.innerDict)
     (dx, dy1) = self.innerDict['pint']
     (dx, dy2) = self.innerDict['dint']
     dy = [i - j for i, j in zip(dy1, dy2)]
     print(dy)
     ax.yaxis.set_offset_position('left')
     i = i + 1
     cValue=float(i)/float(noItems)
     color=str(cValue)
     axlabel= str('diff')
     ax.set_ylim(self.yMin, self.yMax)
     l, = ax.plot(dx, dy, next(linecycler), ms=5, color='black',label=axlabel, linewidth=2.5)
     lArr.append(l)

     t=ax.yaxis.get_offset_text()
     t.set_size(self.fontSize)
     lgd = plt.legend(handles=lArr, fontsize=self.fontSize,  handlelength=3.5, borderpad=1, loc='upper center', bbox_to_anchor=(1.25,1.0))
     plt.xlabel(self.labelEl1, fontsize=self.fontSize)
     plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
     plt.ylabel('the differnce of intervals width', fontsize=self.fontSize)
     plt.setp(ax.get_xticklabels(), fontsize=self.fontSize)
     plt.setp(ax.get_yticklabels(), fontsize=self.fontSize)
     plt.grid(True)
     plt.grid(True, 'minor')
     plt.show()
     f.savefig(self.outputFileName, bbox_extra_artists=(lgd,), bbox_inches='tight')

def main():
    fName1=str(sys.argv[1])
    fName2=str(sys.argv[2])
    ofName=str(sys.argv[3])
    rc = ResultsContainer()
    yMin=0.0
    yMax=0.0
    if (len(sys.argv) == 6):
       yMin=float(sys.argv[4])
       yMax=float(sys.argv[5])
    rc.setYLimits(yMin, yMax)
    rc.setLinesTitles('pint','dint')
    rc.gatherResults(fName1, 'pint')
    rc.gatherResults(fName2, 'dint')
    rc.setFontSize(8)
    rc.setOutputFileName(ofName)
    
    rc.visualizeResults()

if __name__=="__main__":main()
