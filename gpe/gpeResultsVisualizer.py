import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from collections import defaultdict, OrderedDict
from itertools import cycle
import sys


class ResultsContainer:
   """class for results storage"""
   
   def __init__(self):
     self.innerDict=OrderedDict()
     self.labelEl1="x="
     self.labelEl2="y="
     self.fontSize=12
     self.outputFileName='test.eps'

   def addResult(self, k, v):
     if k not in self.innerDict:
        self.innerDict[k]=list()
     self.innerDict[k].append(v)
  
   def rearrangeResults(self):
     for k in self.innerDict:
       self.innerDict[k].sort(key=lambda x: x[0])
       dx, dy = zip(*self.innerDict[k])
       self.innerDict[k]=(dx, dy)
     self.innerDict=OrderedDict(sorted(self.innerDict.items(), key=lambda t: (t[0], t[1])))
   
   def setLabels(self, lEl1, lEl2):
     self.labelEl1=lEl1
     self.labelEl2=lEl2
   
   def setFontSize(self, fs):
     self.fontSize=fs
   
   def setOutputFileName(self, ofn):
     self.outputFileName=ofn

   def gatherResultsForPoints(self, fname):
     self.innerDict.clear()
     a = np.genfromtxt(fname, delimiter=';')
     noRows = a.shape[0]
     print(a.shape)
     for i in range(noRows):
       dataTuple=tuple(a[i])
       (m, indX, indY, leftEnd, rightEnd, intWidth) = dataTuple
       #m=a[i,0]
       #indX=float(a[i,1])
       #indY=float(a[i,2])
       #leftEnd=a[i,3]
       #rightEnd=a[i,4]
       #intWidth=a[i,5]
       if indX != 1.5:
          continue
       k=(indX,indY)
       v=(m, intWidth)
       self.addResult(k, v)

   def gatherResultsForMX(self, fname):
     self.innerDict.clear()
     self.setLabels('y', 'm')
     a = np.genfromtxt(fname, delimiter=';')
     noRows = a.shape[0]
     print(a.shape)
     for i in range(noRows):
       dataTuple=tuple(a[i])
       (m, indX, indY, leftEnd, rightEnd, intWidth) = dataTuple
       #m=a[i,0]
       #indX=float(a[i,1])
       #indY=float(a[i,2])
       #leftEnd=a[i,3]
       #rightEnd=a[i,4]
       #intWidth=a[i,5]
       if indX != 1.5:
          continue
       k=(indX,m)
       v=(indY, intWidth)
       self.addResult(k, v)
   
   def gatherResultsForMY(self, fname):
     self.innerDict.clear()
     self.setLabels('x', 'm')
     a = np.genfromtxt(fname, delimiter=';')
     noRows = a.shape[0]
     print(a.shape)
     for i in range(noRows):
       dataTuple=tuple(a[i])
       (m, indX, indY, leftEnd, rightEnd, intWidth) = dataTuple
       #m=a[i,0]
       #indX=float(a[i,1])
       #indY=float(a[i,2])
       #leftEnd=a[i,3]
       #rightEnd=a[i,4]
       #intWidth=a[i,5]
       if indY != 1.5:
          continue
       k=(indY,m)
       v=(indX, intWidth)
       self.addResult(k, v)

   def visualizeResults(self):
     f, ax = plt.subplots(figsize=(4, 3), dpi=300)
     ax.yaxis.set_offset_position('left')
     linestyle = '--'
     color = 'cornflowerblue'
     text_style = dict(horizontalalignment='right', verticalalignment='center',
		      fontsize=12, fontdict={'family': 'monospace'})

     #resultsToVisual=OrderedDict(sorted(resultsToVisual.items(), key=lambda t: (t[0], t[1])))
     #parsedResults.sort(key=lambda x: (x[0],x[1]))
     i=1
     noItems=len(self.innerDict)
     lines = ["o-","o--","o-.","o:"]
     linecycler = cycle(lines)
     noStyles=len(lines)
     lArr=[]
     for k in self.innerDict:
        (dx, dy) = self.innerDict[k]
        #print(dx)
        #print(dy)
        cValue=float(i)/float(noItems)
        color=str(cValue)
        #ax.text(-0.5, i, nice_repr(linestyle), **text_style)
        (indX, indY) = k
        axlabel=self.labelEl2 + '='+ str(int(indY))
        #print(axlabel)
        #axlabel=self.labelEl1+str(indX) + " ; " + self.labelEl2 + str(indY)
        ax.xaxis.set_major_locator(MultipleLocator(0.1))
        ax.set_xlim(1, 2)
        l, = ax.plot(dx, dy, next(linecycler), ms=5, color=color,label=axlabel, linewidth=2.5) #linestyle=linestyle, color=color, linewidth=3)
        lArr.append(l)
        #format_axes(ax)
        #ax.set_title(k)
        i=i+1
     t=ax.yaxis.get_offset_text()
     t.set_size(self.fontSize)
     #plt.legend(handles=lArr, fontsize=self.fontSize,  handlelength=5, borderpad=1.5)# loc=1, bbox_to_anchor = (1.5, 0.5))
     lgd = plt.legend(handles=lArr, fontsize=self.fontSize,  handlelength=3.5, borderpad=1, loc='upper center', bbox_to_anchor=(1.2,1.0))
     #plt.save('samplefigure', bbox_extra_artists=(lgd,), bbox_inches='tight')
     plt.xlabel(self.labelEl1, fontsize=self.fontSize)
     plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
     plt.ylabel('the width of the interval', fontsize=self.fontSize)
     plt.setp(ax.get_xticklabels(), fontsize=self.fontSize)
     plt.setp(ax.get_yticklabels(), fontsize=self.fontSize)
     plt.grid(True)
     plt.grid(True, 'minor')
     #plt.show()
     f.savefig(self.outputFileName, bbox_extra_artists=(lgd,), bbox_inches='tight')

def main():
    #test()
    fName=str(sys.argv[1])
    mode=str(sys.argv[2])
    ofName=str(sys.argv[3])
    rc = ResultsContainer()
    if mode=='x':
      rc.gatherResultsForMX(fName)
    else:
      rc.gatherResultsForMY(fName)
    #rc.gatherResultsForPoints(fName)
    rc.rearrangeResults()
    #rc.setLabels("x=", 'm')
    rc.setFontSize(8)
    rc.setOutputFileName(ofName)
    rc.visualizeResults()
    #visualizeFPResults(fName)

if __name__=="__main__":main()
