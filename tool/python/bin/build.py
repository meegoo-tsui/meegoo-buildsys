#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    build.py
#  @brief   编译工具，使用当前路径下的build.ini作为配置文件。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

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
from   inc_make   import make

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 默认编译配置文件名称
build_ini = "build.ini"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## main function.
def main():
	global build_ini

	# start build
	printf.reset()
	time.push(os.path.abspath(__file__))

	# build the project
	make.build_type = arg.build_args()
	build_ini = os.getcwd() + "/" + build_ini
	ini.build_parse(build_ini)
	make.do_makes()

	# end build
	time.pop()
	printf.silence("build done.")
	sys.exit(0)

if __name__ == '__main__':
	main()

