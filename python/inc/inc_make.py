#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    inc_make.py
#  @brief   执行make动作，三部曲。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from inc_printf import printf
from inc_cmd    import cmd
from inc_path   import path
from inc_ini    import ini

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## makefile actions.
class make:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## default build action, 0 - build all, 1 - make clean, 2 - make, 3 - make install.
		self.build_type = 0

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## make clean
	def make_clean(self):
		cmd.do("make clean")
		return

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## make
	def make(self):
		cmd.do("make")
		return

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## make install
	def make_install(self):
		cmd.do("make install")
		return

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## do make actions
	def do_makes(self):
		printf.status("build ...")
		# build all projects
		for i in sorted(ini.build_configIni.sections()):
			printf.silence("build project: " + i)
			temp_path = os.path.expandvars(ini.build_configIni.get(i, ini.build_paths[1][0]))
			path.push()
			path.change(temp_path)
			if self.build_type == 1:
				self.make_clean()
			elif self.build_type == 2:
				self.make()
				self.make_install()
			elif self.build_type == 3:
				self.make_install()
			else:
				self.make_clean()
				self.make()
				self.make_install()
			path.pop()
		return

## object of class make.
make = make()
