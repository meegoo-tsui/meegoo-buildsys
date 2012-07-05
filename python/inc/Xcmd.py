#! /usr/bin/python

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    Xcmd.py
#  @brief   command excute.
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @package Xcmd
#  @brief   command excute.
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/04

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   Xprintf   import printf

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## command excute
class cmd:
	## excute a command
	def do(self, command):
		printf.status("running -> " + command)
		rtn = os.system(command)
		if not rtn == 0:
			printf.error("fail - " + command)
			sys.exit(1)
		return

## object of class cmd
cmd = cmd()

