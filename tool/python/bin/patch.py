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
## buildsys import path
buildsys_import_path = os.environ["BUILD_SYS_PATH"] + "/tool/python"
if buildsys_import_path not in sys.path:
	sys.path.insert(0, buildsys_import_path)
import buildsys_import

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   inc_printf import printf
from   inc_time   import time
from   inc_arg    import arg
from   inc_ini    import ini
from   inc_patch  import patch

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## main function.
def main():

	# start patch
	printf.reset()
	time.push(os.path.abspath(__file__))

	# patch the project
	patch.patch_args = arg.patch_args()
	patch_ini = os.getcwd() + "/" + patch.patch_args['-f']
	ini.build_parse(patch_ini)
	patch.do_patch()

	# end patch
	time.pop()
	printf.silence("patch done.")
	sys.exit(0)

if __name__ == '__main__':
	main()
