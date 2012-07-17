#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    patch.py
#  @brief   编译工具，补丁相关动作。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/09

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.time           import time
from   utils.arg            import arg
from   utils.ini            import ini
from   utils.patch_repos    import patch_repos

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## main function.
def main():

	# start patch
	printf.reset()
	time.push(os.path.abspath(__file__))

	# patch the project
	patch_repos.patch_args = arg.patch_args()
	patch_ini = os.getcwd() + "/" + patch_repos.patch_args['-f']
	ini.build_parse(patch_ini)
	patch_repos.do_patch()

	# end patch
	time.pop()
	printf.silence("patch done.")
	sys.exit(0)

if __name__ == '__main__':
	main()
