#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    inc_patch.py
#  @brief   依据ini配置文件执行源码路径的相关补丁操作。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/09

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   inc_printf   import printf
from   inc_cmd      import cmd
from   inc_ini      import ini

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 依据ini配置文件执行源码路径的相关补丁操作。
class patch:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## 仓库类型 svn、git
		self.repos      = ""
		## 源码路径
		self.in_path    = ""
		## 补丁路径
		self.out_path   = ""
		## 补丁动作 - 0: 打上补丁，1：去除补丁，2：生成补丁
		self.action     = 0
		## 补丁标志文件
		self.flag       = "patch.done"

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 判断是否已经打上补丁
	def is_patched(self):
		## 补丁标志文件
		patch_flag_file = self.in_path + "/" + self.flag
		if os.path.exists(patch_flag_file):
			printf.status("源码补丁已经打上, 可以去除补丁。")
			return 1
		else:
			printf.status("源码补丁没有打上，可以打上补丁。")
			return 0
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 创建补丁标志文件
	def create_flag(self, yes): # yes = 1: create, yes = 0: delete
		## 补丁标志文件
		patch_flag_file = self.in_path + "/" + self.flag
		if yes == 1:
			cmd.do("touch " + patch_flag_file)
		else:
			cmd.do("rm -f " + patch_flag_file)

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 打上补丁
	def patch_on(self):
		printf.silence("源码打上补丁 ...")
		if self.is_patched() == 1:
			printf.error("错误： 源码打上补丁！")
		self.create_flag(1)

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 去除补丁
	def patch_down(self):
		printf.silence("源码去除补丁 ...")
		if self.is_patched() == 0:
			printf.error("错误： 源码去除补丁！")
		self.create_flag(0)

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 生成补丁
	def patch_new(self):
		printf.silence("源码生成补丁 ...")

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	##
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 执行补丁动作
	def do_patch(self):
		printf.status("patch ...")
		# patch all projects
		for i in ini.projects:
			printf.silence("patch project: " + i[0])
			# 设置源码路径
			if i[ini.pos_source + 1 ] == "":
				printf.error("No source path !")
			self.in_path = i[ini.pos_source + 1 ]
			# 设置补丁路径
			if i[ini.pos_patch + 1 ] == "":
				printf.error("No patch path !")
			self.out_path = i[ini.pos_patch + 1 ]

			# 补丁动作
			printf.silence("Patch action - " + str(self.action))
			if self.action == 0:   # 0: 打上补丁
				self.patch_on()
			elif self.action == 1: # 1：去除补丁
				self.patch_down()
			elif self.action == 2: # 2：生成补丁
				self.patch_new()
		return

## patch对象.
patch = patch()
