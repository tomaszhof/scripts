import os
import sys
import subprocess

from multiprocessing import Pool

def checkStatus(resArr):
  for r in resArr:
    (status, msg) = r
    if (status==0):
	print '----------------[ERROR BEGIN]--------------\n'
        print 'MESSAGE: '+msg
	print '----------------[ERROR END]----------------\n'
	return 0
  return 1

def processTask(taskInfo):
    cmdBegin = "./gpe_tester --exp_mode=interval_exp --e=8 --alpha1=1 --alpha2=2 --beta1=1 --beta2=2 "
    (m, iamode) = taskInfo
    outFileName='test_m_'+str(m)+'_'+iamode+'.txt'
    command_line = cmdBegin + '--m=' + str(m) + ' --out_file='+outFileName+ ' --arth_mode=' + iamode
    args = [command_line]
    print 'Result file: ' + outFileName
    p = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE)
    p.wait()
    out, err = p.communicate()
    status = 1
    msg = 'OK'
    if 'error' in out:
	status = 0
	msg = out
    print 'done. Status [err]: ' + str(err) 
    return (status, msg)


def main():
  #step (pool size)
  step = 3
  pool = Pool(processes=step)              # start worker processes
  #rootFolderName = sys.argv[1]
  print "Start experiment " #+ rootFolderName + " ... \n"
  
  #get parameters
  testInfoListPINT = []
  for i in range(2,11):
	testInfoListPINT.append((i*10, 'pint'))
  testInfoListDINT = []
  for i in range(2,11):
	testInfoListDINT.append((i*10, 'dint'))

  #calculation PINT
  currBeg = 0
  currEnd = 0
  maxL = len(testInfoListPINT)
  while currEnd < maxL :
    subList = testInfoListPINT[currBeg:currEnd]
    currBeg = currEnd
    currEnd = currEnd + step - 1 
    resArr = pool.map(processTask,subList)
    status = checkStatus(resArr)
    print 'Caluclate ' + str(currEnd) + '/' + str(maxL) + 'tasks.'
    if (status == 0):
      break

  rest = maxL - int(maxL/step)*step;
  subList = testInfoListPINT[maxL-rest:maxL]
  resArr = pool.map(processTask,subList)
  status = checkStatus(resArr)
  print 'Caluclate ' + str(currEnd) + '/' + str(maxL) + 'tasks.'
  
  #calculation DINT
  currBeg = 0
  currEnd = 0
  maxL = len(testInfoListDINT)
  while currEnd < maxL :
    subList = testInfoListDINT[currBeg:currEnd]
    currBeg = currEnd
    currEnd = currEnd + step - 1 
    resArr = pool.map(processTask,subList)
    status = checkStatus(resArr)
    print 'Caluclate ' + str(currEnd) + '/' + str(maxL) + 'tasks.'
    if (status == 0):
      break

  rest = maxL - int(maxL/step)*step;
  subList = testInfoListDINT[maxL-rest:maxL]
  resArr = pool.map(processTask,subList)
  status = checkStatus(resArr)
  print 'Caluclate ' + str(currEnd) + '/' + str(maxL) + 'tasks.'
  print "Completed."

if __name__=="__main__":main()
