#! /usr/bin/python

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    inc_cmd.py
#  @brief   command excute.
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   inc_printf   import printf

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

	## try excute a command
	def tryit(self, command):
		printf.status("try running -> " + command)
		os.system(command)
		return

## object of class cmd
cmd = cmd()

