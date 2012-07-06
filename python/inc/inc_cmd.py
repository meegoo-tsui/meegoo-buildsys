#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    inc_cmd.py
#  @brief   在python执行其他shell命令。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   inc_printf   import printf

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 执行shell命令。
class cmd:
	## 执行shell命令，不成功就强制退出。
	def do(self, command):
		printf.status("running -> " + command)
		rtn = os.system(command)
		if not rtn == 0:
			printf.error("fail - " + command)
			sys.exit(1)
		return

	## 执行shell命令，不成功不强制退出。
	def tryit(self, command):
		printf.status("try running -> " + command)
		os.system(command)
		return

## cmd对象
cmd = cmd()

