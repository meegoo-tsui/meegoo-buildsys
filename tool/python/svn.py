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
from   utils.cmd            import cmd

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
	# Clean all svn repos at current path
	elif svn_args == "-c":
		current_path = os.getcwd()
		for r in os.walk(current_path).next()[1]:
			rev = os.popen("svn info " + r + " | awk '/Revision:/ { print $2 }'").read()
			rev = "-svn" + rev.split("\n")[0]			
			# patch backup
			cmd.tryit("svn st " + r + " | grep '^M' | awk '{print $2}' | xargs svn revert ")
			cmd.tryit("svn st " + r + " | grep '^?' | awk '{print $2}' | xargs rm -rf ")
			cmd.tryit("find "   + r + " -name \"*.o\" | xargs rm -f")
			cmd.tryit("svn up " + r)
	# backup all svn repos at current path
	elif svn_args == "-b":
		current_path = os.getcwd()
		for r in os.walk(current_path).next()[1]:
			rev = os.popen("svn info " + r + " | awk '/Revision:/ { print $2 }'").read()
			rev = "-svn" + rev.split("\n")[0]
			cmd.tryit("tar -jcf " + r + rev + ".tar.bz2 " + r)
	elif svn_args == "-s":
		printf.status("svn info")
		os.system("svn info")

	sys.exit(0)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if __name__ == '__main__':
	main()
