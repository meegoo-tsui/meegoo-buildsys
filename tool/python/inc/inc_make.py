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
from   inc_printf import printf
from   inc_cmd    import cmd
from   inc_path   import path
from   inc_ini    import ini
from   inc_wfile  import wfile

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
	def make_clean(self, project_args):
		wfile.wmakefile(project_args)
		cmd.do("make clean")
		return

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## make
	def make(self, project_args):
		wfile.wmakefile(project_args)
		cmd.do("make all")
		return

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## make install
	def make_install(self, project_args):
		wfile.wmakefile(project_args)
		cmd.do("make install")
		return

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## do make actions
	def do_makes(self):
		printf.status("build ...")
		# build all projects
		for i in ini.projects:
			printf.silence("build project: " + i[0])
			makefile_path = i[ini.pos_makefile + 1]
			path.push()
			path.change(makefile_path)
			if self.build_type == 1:
				self.make_clean(i)
			elif self.build_type == 2:
				self.make(i)
				self.make_install(i)
			elif self.build_type == 3:
				self.make_install(i)
			else:
				self.make_clean(i)
				self.make(i)
				self.make_install(i)
			path.pop()
		return

## object of class make.
make = make()
