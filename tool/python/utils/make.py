#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    make.py
#  @brief   执行make动作，三部曲。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.glb            import glb
from   utils.cmd            import cmd
from   utils.path           import path
from   utils.build_ini      import build_ini
from   utils.wfile          import wfile
from   utils.patch_repos    import patch_repos

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## makefile actions.
class make:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## build 参数字典
		self.build_args = {}

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## make others
	def make_others(self, project_dict):
		wfile.wmakefile(project_dict)
		cmd.do("make others " + "prjs=\"" + self.build_args['-x'] + "\"")
		return

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
		for i in build_ini.list_of_dict:
			printf.silence("build project: " + i[glb.project_name])
			project_path = i[glb.project_path]
			path.push()
			path.change(project_path)

			# 缺省无参数 - clean、make、install
			action_sum = self.build_args['-c'] + self.build_args['-m'] + self.build_args['-i']
			
			# 执行相关make动作之前，先打上补丁
			patch_repos.patch_args = {"-f":build_ini.ini, "-p": i[glb.project_name], "-a":0}
			patch_repos.do_patch()
			
			# make others, 执行完后返回
			if self.build_args['-x'] != '':
				self.make_others(i)
				return

			# make clean
			if self.build_args['-c'] == 1 or action_sum == 0:
				self.make_clean(i)

			# make
			if self.build_args['-m'] == 1 or action_sum == 0:
				self.make(i)

			# make install
			if self.build_args['-i'] == 1 or action_sum == 0:
				self.make_install(i)

			path.pop()
		return

## object of class make.
make = make()
