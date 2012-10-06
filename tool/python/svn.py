#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    svn.py
#  @brief   svn工具，显示相关异常文件。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/10/06

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.arg            import arg

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## main function.
def main():

	svn_args = arg.repos_args("svn")
	if svn_args == "-m":
		os.system("svn st | grep '^M' | awk '{print $2}'")
	elif svn_args == "-d":
		os.system("svn st | grep '^!' | awk '{print $2}'")
	elif svn_args == "-o":
		os.system("svn st | grep '^?' | awk '{print $2}'")	
	
	sys.exit(0)

if __name__ == '__main__':
	main()
