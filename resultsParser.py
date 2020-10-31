import sys
import os
import string
import re
from collections import defaultdict
from os import listdir
from os.path import isfile, join, basename

class ResultFileParser:
  def __init__(self):
    self.listOfFiles=[]
    self.parsedResults = defaultdict(list)
    self.outSep=';'

  def getFiles(self, dirPath, filesExt, filesBeg):
    listdir(dirPath)
    print filesExt
    for f in listdir(dirPath):
      if (isfile(join(dirPath,f)) and f.endswith(filesExt)):
        print f
    listOfFiles = [ f for f in listdir(dirPath) if (isfile(join(dirPath,f)) and f.endswith(filesExt)
    and f.startswith(filesBeg)) ]
    return listOfFiles
   
  def parseFile(self, dirPath, fileName):
    resBeginLineNo=8
    step=4
    f = open(dirPath+'/'+fileName)
    lines = f.readlines()
    f.close()
    baseName=basename(fileName).split('.')[0]
    nameArr=baseName.split('_')
    gridSize=0
    arthId='none'
    if (len(nameArr)>2):
      gridSize=nameArr[2]
      arthId=nameArr[3]
    resLines=lines #[resBeginLineNo:]
    linesNo = len(resLines)
    pointRegex=re.compile('\(([^]]*)\)')
    intervalRegex=re.compile('\[([^]]*)\]')
    floatRegex=re.compile('[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?')
    resultsList=list()
    i=0
    while (i<linesNo):
      line=resLines[i]
      if 'u(' not in line:
        i=i+1
        continue
      lineWidth=resLines[i+1]
      lineExact=resLines[i+2]
      i=i+3

      points = pointRegex.findall(line)
      interval= intervalRegex.findall(line)
      print interval                  
      iends=floatRegex.findall(str(interval))
      ipoint=floatRegex.findall(str(points))
      iwidth=floatRegex.findall(lineWidth) #.split('=', 1)[-1])
      iexact=floatRegex.findall(lineExact) #.split('=', 1)[-1])

      leftTuple=iends[0]
      rightTuple=iends[1]
      widthTuple=iwidth[0]
      pointXTuple=ipoint[0]
      pointYTuple=ipoint[1]
      uExactTuple=iexact[2]

      intLeft=leftTuple[0]+leftTuple[2]
      intRight=rightTuple[0]+rightTuple[2]
      intWidth=widthTuple[0]+widthTuple[2]
      intPX = pointXTuple[0]+pointXTuple[2]
      intPY = pointYTuple[0]+pointYTuple[2]
      u_exact = uExactTuple[0]+uExactTuple[2]

      resultsList.append(((intPX, intPY), (intLeft, intRight), intWidth,u_exact))


    resultsList = sorted(resultsList, key=lambda tup:(tup[0], tup[1]))
    resTuple=(int(gridSize), resultsList)
    #add results to dictionary
    print('Grid size: ' + str(gridSize))
    if arthId not in self.parsedResults:
      print('Created new list for arthId.')
      self.parsedResults[arthId]=list()
    self.parsedResults[arthId].append(resTuple)
    
    self.parsedResults[arthId] = sorted(self.parsedResults[arthId], key=lambda tup:(tup[0], tup[1]))


    return resTuple

  def saveResultsInCsv(self, fName):
    sep = self.outSep
    for arthId, resTupleList in self.parsedResults.items():
      outFileName=fName+'_'+str(arthId)+'.csv'
      outFile=open(outFileName, 'w')
      
      for resTuple in resTupleList:
        (gridSize, resultsList)=resTuple
        for r in resultsList:
          (resPoint, resInt, resIntWidth, u_exact)=r
          (pX, pY)=resPoint
          (iL, iR)=resInt
          resLine=''
          resLine+=str(gridSize)+sep+str(pX)+sep+str(pY)+sep+str(iL)+sep+str(iR)+sep+resIntWidth+sep+str(u_exact)+'\n'
          outFile.write(resLine)
      outFile.close()


def main():
  dirPath = str(sys.argv[1])
  print(dirPath)
  filesExt=str(sys.argv[2])
  filesBeg=str(sys.argv[3])
  resultsFileName=str(sys.argv[4])
  p = ResultFileParser()
  files = p.getFiles(dirPath, filesExt, filesBeg)
  print(files)
  for fName in files:
    print('Parsing file: ' + fName + '...')
    p.parseFile(dirPath, fName)
    print ('file parsed.')
  p.saveResultsInCsv(resultsFileName) 

if __name__=="__main__":main()