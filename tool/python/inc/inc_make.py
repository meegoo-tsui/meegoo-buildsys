#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    inc_make.py
#  @brief   执行make动作，三部曲。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   inc_printf import printf
from   inc_glb    import glb
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
		## build 参数字典
		self.build_args = {}

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## make clean
	def make_clean(self, project_dict):
		wfile.wmakefile(project_dict)
		cmd.do("make clean")
		return

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## make
	def make(self, project_dict):
		wfile.wmakefile(project_dict)
		cmd.do("make all")
		return

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## make install
	def make_install(self, project_dict):
		wfile.wmakefile(project_dict)
		cmd.do("make install")
		return

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## do make actions
	def do_makes(self):
		printf.status("build ...")
		# build all projects
		for i in ini.list_of_dict:
			printf.silence("build project: " + i[glb.project_name])
			project_path = i[glb.project_path]
			path.push()
			path.change(project_path)

			# 缺省无参数 - clean、make、install
			sun = self.build_args['-c'] + self.build_args['-m'] + self.build_args['-i']
			
			# make clean
			if self.build_args['-c'] == 1 or sun == 0:
				self.make_clean(i)

			# make
			if self.build_args['-m'] == 1 or sun == 0:
				self.make(i)

			# make install
			if self.build_args['-i'] == 1 or sum == 0:          
				self.make_install(i)

			path.pop()
		return

## object of class make.
make = make()
