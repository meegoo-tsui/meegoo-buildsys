#! /usr/bin/python

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    build.py
#  @brief   build projects via build.ini.
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## buildsys import path
buildsys_import_path = os.environ["BUILD_SYS_PATH"] + "/python"
if buildsys_import_path not in sys.path:
     sys.path.insert(0, buildsys_import_path)
import buildsys_import

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from inc_printf import printf
from inc_time   import time
from inc_arg    import arg
from inc_ini    import ini
from inc_make   import make

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## main function.
def main():
	
	# start build
	printf.reset()
	time.push(os.path.abspath(__file__))

	# build the project
	make.build_type = arg.build_args()
	ini.build_parse()
	make.do_makes()

	# end build
	time.pop()
	printf.silence("all done.")
	sys.exit(0)

if __name__ == '__main__':
	main()

