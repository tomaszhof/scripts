import os
import sys
import subprocess
from os.path import isfile, join, basename

def main():
  dirPath = str(sys.argv[1])
  begName = str(sys.argv[2])

  for filename in os.listdir(dirPath):
    if filename.startswith(begName):
      baseName=basename(filename)
      nameArr=baseName.split('_')
      exName=nameArr[0]
      gridSize=nameArr[3]
      newFileName=exName + '_m_' + gridSize + '_' + nameArr[1] + '.txt'
      os.rename(filename, newFileName)

if __name__=="__main__":main()
