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
    listOfFiles = [ f for f in listdir(dirPath) if (isfile(join(dirPath,f)) and f.endswith(filesExt)
    and f.startswith(filesBeg)) ]
    return listOfFiles
   
  def parseFile(self, fileName):
    resBeginLineNo=8
    step=4
    f = open(fileName)
    lines = f.readlines()
    f.close()
    baseName=basename(fileName)
    nameArr=baseName.split('_')
    gridSize=0
    arthId='none'
    if (len(nameArr)>2):
      #print(len(nameArr))
      gridSize=nameArr[2]
      arthId=nameArr[3]
    resLines=lines[resBeginLineNo:]
    linesNo = len(resLines)
    pointRegex=re.compile('\(([^]]*)\)')
    intervalRegex=re.compile('\[([^]]*)\]')
    floatRegex=re.compile('[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?')
    resultsList=list()
    i=0
    while (i<linesNo):
      line=resLines[i]
      lineWidth=resLines[i+1]
      i=i+step
      points = pointRegex.findall(line)
      interval= intervalRegex.findall(line)                   
      iends=floatRegex.findall(str(interval))
      ipoint=floatRegex.findall(str(points))
      iwidth=floatRegex.findall(lineWidth)
      #print(line+'n')
      #print(interval)
      #print(iends)
      leftTuple=iends[0]
      rightTuple=iends[1]
      widthTuple=iwidth[0]
      pointXTuple=ipoint[0]
      pointYTuple=ipoint[1]
      intLeft=leftTuple[0]+leftTuple[2]
      intRight=rightTuple[0]+rightTuple[2]
      intWidth=widthTuple[0]+widthTuple[2]
      intPX = pointXTuple[0]+pointXTuple[2]
      intPY = pointYTuple[0]+pointYTuple[2]
      #print(intLeft)
      #print(intRight)
      #print(intWidth)
      #print(intPX)
      #print(intPY)
      #print(gridSize)
      resultsList.append(((intPX, intPY), (intLeft, intRight), intWidth))

    resTuple=(gridSize, resultsList)
    #add results to dictionary
    self.parsedResults[arthId].append(resTuple)

    return resTuple

  def saveResultsInCsv(self, fName):
    sep = self.outSep
    for arthId, resTuple in self.parsedResults.items():
      outFileName=fName+str(arthId)+'.csv'
      outFile=open(outFileName, 'w')
      resLine=''
      #print(resTuple)
      (gridSize, resultsList)=resTuple[0]
      for r in resultsList:
        (resPoint, resInt, resIntWidth)=r
        (pX, pY)=resPoint
        (iL, iR)=resInt
        resLine+=str(pX)+sep+str(pY)+sep+str(iL)+sep+str(iR)+sep+resIntWidth+'\n'
        outFile.write(resLine)
      outFile.close()


def main():
  print('main test')
  inputFileName = sys.argv[1]
  dirPath = sys.argv[2]
  print('main test')
  p = ResultFileParser()
  res=p.parseFile(inputFileName)
  filesExt=".txt"
  filesBeg="test"
  files = p.getFiles(dirPath, filesExt, filesBeg)
  print(files)
  for fName in files:
    print('Parsing file: ' + fName + '...')
    p.parseFile(fName)
    print ('file parsed.')
  p.saveResultsInCsv('results') 
  #print(res)
if __name__=="__main__":main()
