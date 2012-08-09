#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    check.py
#  @brief   下载工具，check out相关动作。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/08/09

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.time           import time
from   utils.arg            import arg
from   utils.check_repos    import check_repos

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## main function.
def main():

	# start patch
	time.push(os.path.abspath(__file__))

	# check out the project
	check_repos.check_args = arg.check_args()
	ini = os.getcwd() + "/" + check_repos.check_args['-f']
	check_repos.check_out(ini)

	# end patch
	time.pop()
	printf.silence("check out done.")
	sys.exit(0)

if __name__ == '__main__':
	main()
