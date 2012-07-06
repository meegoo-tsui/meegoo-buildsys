#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    inc_arg.py
#  @brief   所有工具的参数解析及帮助信息。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys
import getopt

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   inc_printf   import printf

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 参数解析、帮助信息。
class arg:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具build.py的帮助信息。
	def build_usage(self):
		printf.printf(3, "Usage:\n" + "build.py " + "[options]")
		printf.printf(3, '''
Options:
-h | --help  print help info
-c           make clean
-m           make
-i           make install
default      make clean, make, make install
''')

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具build.py的解析参数。
	def build_args(self):
		printf.status("parse args ...")
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hcmi", ["help"])
		except getopt.GetoptError as err:
			printf.warn(str(err)) # will print something like "option -a not recognized"
			self.build_usage()
			sys.exit(1)

		build_type = 0
		for o, a in opts:
			if   o in ("-h", "--help"):
				self.build_usage()
				sys.exit(1)
			elif o == "-c":
				build_type = 1
			elif o == "-m":
				build_type = 2
			elif o == "-i":
				build_type = 3
			else:
				assert False, "unhandled option"
				self.build_usage()
				sys.exit(1)
		return build_type

## arg对象。
arg = arg()
