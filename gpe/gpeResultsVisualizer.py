import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict, OrderedDict
from itertools import cycle


class ResultsContainer:
   """class for results storage"""
   
   def __init__(self):
     self.innerDict=OrderedDict()
     self.labelEl1="x="
     self.labelEl2="y="

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

   def gatherResultsForPoints(self, fname):
     self.innerDict.clear()
     a = np.genfromtxt(fname, delimiter=';')
     noRows = a.shape[0]
     print(a.shape)
     for i in range(noRows):
       m=a[i,0]
       indX=float(a[i,1])
       indY=float(a[i,2])
       leftEnd=a[i,3]
       rightEnd=a[i,4]
       intWidth=a[i,5]
       if indX != 1.5:
          continue
       k=(indX,indY)
       v=(m, intWidth)
       self.addResult(k, v)

   def gatherResultsForM(self, fname):
     self.innerDict.clear()
     a = np.genfromtxt(fname, delimiter=';')
     noRows = a.shape[0]
     print(a.shape)
     for i in range(noRows):
       m=a[i,0]
       indX=float(a[i,1])
       indY=float(a[i,2])
       leftEnd=a[i,3]
       rightEnd=a[i,4]
       intWidth=a[i,5]
       if indX != 1.5:
          continue
       k=(indX,m)
       v=(indY, intWidth)
       self.addResult(k, v)

   def visualizeResults(self):
     f, ax = plt.subplots()
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
        print(dx)
        print(dy)
        cValue=float(i)/float(noItems)
        color=str(cValue)
        #ax.text(-0.5, i, nice_repr(linestyle), **text_style)
        (indX, indY) = k
        axlabel=self.labelEl1+str(indX) + " ; " + self.labelEl2 + str(indY) 
        l, = ax.plot(dx, dy, next(linecycler), color=color,label=axlabel) #linestyle=linestyle, color=color, linewidth=3)
        lArr.append(l)
        #format_axes(ax)
        #ax.set_title(k)
        i=i+1
     plt.legend(handles=lArr, loc=1)
     plt.xlabel('m=n')
     plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
     plt.ylabel('width of the results interval')
     plt.grid(True)
     plt.show()


def main():
    #test()
    fName='results_pint.txt.csv'
    rc = ResultsContainer()
    rc.gatherResultsForM(fName)
    rc.gatherResultsForPoints(fName)
    rc.rearrangeResults()
    rc.setLabels("x=", "y=")
    rc.visualizeResults()
    #visualizeFPResults(fName)

if __name__=="__main__":main()
