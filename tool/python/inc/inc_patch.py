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
from   inc_ini      import ini

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 依据ini配置文件执行源码路径的相关补丁操作。
class patch:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## 源码路径
		self.in_path    = ""
		## 补丁路径
		self.out_path   = ""
		## 补丁动作 - 0: 打上补丁，1：去除补丁，2：生成补丁
		self.action     = 0
	
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
		return

## patch对象.
patch = patch()
