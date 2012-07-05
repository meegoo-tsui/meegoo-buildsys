#! /usr/bin/python

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    Xpath.py
#  @brief   path package.
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   Xprintf   import printf

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## path change.
class path:
	## The constructor.
	def __init__(self):
		## a stack for store the path
		self.pathstack = []

	## change path
	def change(self, new_path):
		os.chdir(new_path)
		return

	## push path to stack
	def push(self):
		pathstack.append(os.getcwd())
		return

	## pop path from stack
	def pop(self):
		if len(self.pathstack) == 0:
			printf.error(os.path.abspath(__file__) + ": len(pathstack) is 0")
			sys.exit(1)
		self.change(pathstack.pop())
		return

## object of class path.
path = path()

