#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    path.py
#  @brief   路径切换，堆栈操作形式。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf   import printf

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## path change.
class path:
	## The constructor.
	def __init__(self):
		## a stack for store the path
		self.pathstack = []

	## get current path
	def get(self):
		return os.getcwd()

	## change path.
	def change(self, new_path):
		if not os.path.isdir(new_path):
			printf.error(new_path + " - " + " not a path !")
		printf.status("change path: " + new_path)
		os.chdir(new_path)
		return

	## push path to stack.
	def push(self):
		self.pathstack.append(os.getcwd())
		printf.status("path push - " + os.getcwd())
		return

	## pop path from stack.
	def pop(self):
		if len(self.pathstack) == 0:
			printf.error(os.path.abspath(__file__) + ": len(pathstack) is 0")
			sys.exit(1)
		self.change(self.pathstack.pop())
		return

## object of class path.
path = path()
