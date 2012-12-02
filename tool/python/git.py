#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    git.py
#  @brief   git工具，显示相关异常文件。
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

	svn_args = arg.repos_args("git")
	if svn_args == "-m":
		os.system("git status -s | grep '^ M' | awk '{print $2}'")
	elif svn_args == "-d":
		os.system("git status -s | grep '^ D' | awk '{print $2}'")
	elif svn_args == "-o":
		os.system("git status -s | grep '^??' | awk '{print $2}'")	
	elif svn_args == "-s":
		printf.status("Remote URL:")
		os.system("git remote -v")
		printf.status("Remote Branches: ")
		os.system("git branch -r")
		if os.path.isfile(".git/config"):
			printf.status("== Configuration .git/config")
			os.system("cat .git/config")
		printf.status("== Most Recent Commit")
		os.system("git --no-pager log --max-count=1")

	sys.exit(0)

if __name__ == '__main__':
	main()
