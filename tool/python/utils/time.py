#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    time.py
#  @brief   时间戳及运行计时功能，堆栈操作计时。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys
from   datetime import datetime

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf  import printf

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## timer and timestamp
class time:
	## The constructor.
	def __init__(self):
		## a stack for store the timestamp - ("message ...", datetime.now())
		self.timestack = []

	## return a timestamp
	def timestamp(self):
		timestamp = str(datetime.now())
		timestamp = timestamp.split(".")[0]
		timestamp = timestamp.replace(" ","_")
		timestamp = timestamp.replace(":","-")
		return timestamp

	## push timestamp to stack
	def push(self,message):
		data = (message, datetime.now())
		self.timestack.append(data)
		return

	## pop timestamp from stack
	def pop(self):
		if len(self.timestack) == 0:
			printf.error(os.path.abspath(__file__) + ": len(timestack) is 0")
			sys.exit(1)
		data      = time.timestack.pop()
		now       = datetime.now()
		timer     = now - data[1]
		str_timer = " - " + str(timer.seconds/3600) + 'h:' \
		            + str(timer.seconds%3600/60) + 'm:' \
		            + str(timer.seconds%60) + 's'
		printf.status(data[0] + str_timer)
		return

## object of class time
time = time()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Test all packages.
def main():

	printf.reset()
	time.push(os.path.abspath(__file__))
	time.pop()

	sys.exit(0)

if __name__ == '__main__':
	main()
