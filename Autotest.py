#$language = "Python"
#$interface = "1.0"


# Copyright (c) 2018 chenfufeng <chenfufeng@ruijie.com.cn>
#
# Support for Python 2.7 or Higher version and for SecureCRT higher than 7 Version
#
# The code is available at
#   https://github.com/cff874460349/IOT_AutoTest.git
#
# Function:
#   1、Support LoRa\NB-IOT module or more
#   2、Execute command and get test result in script
#   3、Collect Error Log for every command
#   4、Generate test report after script running

# This shows a simple example of waiting for a message to be published.


import sys
import os
import time
import csv
import codecs



#logPath =  crt.Dialog.FileOpenDialog("please open a Path","open")
filePath = crt.Dialog.FileOpenDialog("Please select a TestCase file","Open",  filter = "Txt Files (*.txt)|*.txt") 

currPath = 'E:\\AutoTestLog\\'

currTime = time.strftime('%Y%m%d_%H_%M_%S',time.localtime(time.time()))
reportPath = currPath + "TestReport_%s.csv" %(currTime)
reportFile = open(reportPath, 'ab+')
reportFile.write(codecs.BOM_UTF8)
writer = csv.writer(reportFile)
reportTitle = ['脚本编号', '测试用例编号', '测试用例名称', '测试步骤及结果', '测试结果']
writer.writerow(reportTitle)
#reportFile.close()

#等待所有执行结果
def execute_and_result(cmd, waitResultList, sleep_time=6): 
    waitAllResult = True   
    crt.Screen.Send(cmd + "\r\n")
    for waitResult in waitResultList:
    	wait_result = crt.Screen.WaitForStrings(waitResult, sleep_time)
    	waitAllResult = wait_result * waitAllResult
    return waitAllResult


#等待其中一个执行结果
def execute_or_result(cmd, waitResultList, sleep_time=6):
	crt.Screen.Send(cmd + "\r\n")
	wait_result = crt.Screen.WaitForStrings(waitResultList, sleep_time)    
	return wait_result


#create Log when error occurate
def create_ErrorLog(TestCase, SubCase, step, cmd):
	#get current COM message to getScr
	maxRows = crt.Screen.Rows
	maxCols = crt.Screen.Columns
	getScr = crt.Screen.Get2(-10, 1, maxRows, maxCols)
	#get current system time
	currTime = time.strftime('%Y%m%d_%H_%M_%S',time.localtime(time.time()))
	#generate E:\AutoTestLog\TestCase_time.txt
	if len(SubCase) > 0:
		logPath = currPath + "%s_%s_Step%d_%s.txt" %(TestCase, SubCase, step, currTime)
	else:
		logPath = currPath + "%s_Step%d_%s.txt" %(TestCase, step, currTime)
	#crt.Dialog.MessageBox("%s" %logPath)
	logfile = open(logPath, 'a')
	for line in getScr:
		logfile.write(line)
	logfile.close()


def execute_get_result(cmd, result):
	isSuccess = True
	resultList = result.split('&')		
	crt.Sleep(5000)		
	if len(resultList) > 1:
		#预期结果是有&(与)关系
		isSuccess = execute_and_result(cmd, resultList)
	else:
		#预期结果是有or(或)关系
		resultList = result.split('|')
		isSuccess = execute_or_result(cmd, resultList)
	if True == isSuccess:
		return "PASS"
	else:
		return "FAIL"


def create_TestReport(TestCase, TestID, TestName, cmdResult, TestResult):
	if "" == TestCase:
		return
	reportTitle = [TestCase, TestID, TestName, cmdResult, TestResult]
	writer.writerow(reportTitle)
	return


def execute_cmd(filePath):
	#read 
	file = open(filePath, "r")
	lines = file.readlines()
	step = 0
	TestCase=""
	SubCase=""
	TestResult=""
	cmdResult=""
	TestID=""
	TestName=""
	for line in lines:
		line = line.strip()
		#判断是否是空行或注释行  
		if not len(line) or line.startswith('#'):
			continue                            #是的话，跳过不处理  
		if line.startswith('TestCase'):
			#create last TestCase result
			create_TestReport(TestCase, TestID, TestName, cmdResult, TestResult)
			lineStr = line.decode('gb2312').encode('utf-8')
			#crt.Dialog.MessageBox("%s" %(lineStr))
			[TestCase, TestID, TestName] = lineStr.split()
			crt.Sleep(3000)
			crt.Screen.Clear()
			#init every TestCase
			step = 0
			TestResult="PASS"
			cmdResult = ""
			continue

		#get SubCase No.
		if line.startswith('SubCase'):
			SubCase = line
			cmdResult = cmdResult + "\r\n\r\n" + SubCase + "\r\n"
			crt.Sleep(3000)
			crt.Screen.Clear()
			step = 0
			continue

		#delay delayTime between steps
		if line.startswith('delay'):
			[delay, delayTime] = line.split()
			crt.Sleep(int(delayTime))
			continue	

		[cmd, result] = line.split()
		step += 1		
		isSuccess = execute_get_result(cmd, result)		
		if isSuccess == "FAIL":
			#当发生错误的时候保存当前串口页面的日志
			create_ErrorLog(TestCase, SubCase, step, cmd)
			TestResult="FAIL"
			#crt.Dialog.MessageBox("%s: %s Fail !" %(TestCase, cmd))
		cmdResult = (cmdResult + "Step%d:" + cmd + "," + isSuccess + "\r\n")  %(step)
	create_TestReport(TestCase, TestID, TestName, cmdResult, TestResult)
	crt.Dialog.MessageBox("All TestCase Run Finish! \r\n Log:E:\AutoTestLog")
	file.close()
	

def main():
	try:
		if "" == filePath:
			crt.Dialog.MessageBox("AutoTest Run Fail! No AutoScript To Run!")
			raise
		execute_cmd(filePath)
		reportFile.close()
	except Exception as e:
		reportFile.close()
	else:
		pass
	finally:
		pass

		
main()
#execute_cmd(filePath)
#reportFile.close()