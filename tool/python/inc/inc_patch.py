#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    inc_patch.py
#  @brief   依据ini配置文件执行源码路径的相关补丁操作。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/09

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, glob

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   inc_printf   import printf
from   inc_glb      import glb
from   inc_cmd      import cmd
from   inc_path     import path
from   inc_ini      import ini
from   inc_time     import time

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 对应仓库命令
patch_cmd = {}

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 依据ini配置文件执行源码路径的相关补丁操作。
class patch:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## patch 参数字典
		self.patch_args = {}
		## 源码路径
		self.in_path    = ""
		## 补丁路径
		self.out_path   = ""
		## repos根目录
		self.top_path   = ""
		## 补丁动作 - 0: 打上补丁，1：去除补丁，2：生成补丁
		self.action     = 0
		## 补丁标志文件
		self.flag       = "patch.done"
		## git补丁命令
		self.cmd_git    = {
						    "list_modify":  "git ls-files -m",
						    "list_untrack": "git ls-files -o",
						    "diff":         "git diff",
						    "level":        "  -p1 <  "
						  }
		## svn补丁命令
		self.cmd_svn    = {
						    "list_modify":  "svn status | grep \"^M\" | awk \'{print $2}\'",
						    "list_untrack": "svn status | grep \"^?\" | awk \'{print $2}\'",
						    "diff":         "svn diff",
						    "level":        "  -p0 <  "
						  }

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 判断是否已经打上补丁
	def is_patched(self):
		## 补丁标志文件
		patch_flag_file = self.in_path + "/" + self.flag
		if os.path.exists(patch_flag_file):
			printf.status("可以去除补丁。")
			return 1
		else:
			printf.status("可以打上补丁。")
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
	## 0 - 打上补丁， 1 - 去除补丁
	def patch(self, _a):
		global patch_cmd

		if _a == 0:
			printf.silence("执行对源码打上补丁 ...")
			if self.is_patched() == 1:
				printf.error("错误： 源码已打上补丁！")
			end_flag = ""
		else:
			printf.silence("执行对源码去除补丁 ...")
			if self.is_patched() == 0:
				printf.error("错误： 源码已去除补丁！")	
			end_flag = " -R"

		# 补丁类表
		patch_list = []
		patch_list.extend(glob.glob(self.out_path + "/*" + glb.patch_filetype))
		# 处理所有补丁
		for i in patch_list:
			# git和svn产生的补丁路径不一样，区别对待
			if i.find("git-") != -1:
				level = self.cmd_git['level']
			else:
				level = patch_cmd['level']
			cmd.do("patch -d " + self.top_path + level + i + end_flag)

		# 完成
		self.create_flag(not _a) # 标志文件处理
		printf.status("补丁操作完成。")

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 生成补丁
	def patch_new(self):
		global patch_cmd
		printf.silence("源码生成补丁 ...")
		# 备份以前存在的补丁
		if os.path.isdir(self.out_path):
			patch_list_old = []
			old_patchs = self.out_path + "/*" + glb.patch_filetype
			patch_list_old.extend(glob.glob(old_patchs))
			if len(patch_list_old) > 0:
				patch_bak_path = self.out_path + "/" + time.timestamp()
				cmd.do("mkdir -p " + patch_bak_path)
				cmd.do("mv " + old_patchs + " " + patch_bak_path)

		out_modify  = os.popen(patch_cmd['list_modify']).read()
		out_untrack = os.popen(patch_cmd['list_untrack']).read()

		# 生成修改文件补丁
		patch_list = out_modify.split("\n")
		printf.status("Modify files: " + str(len(patch_list) - 1))
		for i in patch_list:
			if i == "":
				continue
			name = self.out_path + "/" + self.patch_args['-r'] + "-" + i.replace("/","_")
			cmd.do(patch_cmd['diff'] + " " + i + " > " + name + glb.patch_filetype)

		# 生成未托管文件补丁
		patch_list = out_untrack.split("\n")
		printf.status("Untrack files: " + str(len(patch_list) - 1))
		for i in patch_list:
			if i == "" or i.find(self.flag) != -1:
				continue
			name = self.out_path + "/" + "git-" + i.replace("/","_")
			cmd.tryit("git diff /dev/null " + i + " > " + name + glb.patch_filetype)

		# 完成操作退出
		self.create_flag(1)

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 执行补丁动作
	def do_patch(self):
		global patch_cmd

		printf.status("patch ...")
		# patch all projects
		for i in ini.list_of_dict:
			printf.silence("patch project: " + i[glb.project_name])
			# 设置源码路径
			if not i.has_key(glb.source_path):
				printf.error("No source path !")
			self.in_path = i[glb.source_path]
			# 设置补丁路径
			if not i.has_key(glb.patch_path):
				printf.error("No patch path !")
			self.out_path = i[glb.patch_path]

			# 创建补丁路径
			if not os.path.isdir(self.out_path):
				cmd.do("mkdir -p " + self.out_path)
			
			# 切换路径
			path.push()
			path.change(self.in_path)

			# 设置仓库命令
			self.top_path = self.in_path # 默认为根路径
			if self.patch_args['-r'] == "svn":
				patch_cmd = self.cmd_svn
			elif self.patch_args['-r'] == "git":
				patch_cmd     = self.cmd_git
				self.top_path = os.popen("git rev-parse --show-toplevel").read().split("\n")[0]
			else:
				printf.error("repos type error - " + self.patch_args['-r'])

			# 补丁动作
			self.action = self.patch_args['-a']
			printf.silence("Patch action - " + str(self.action))
			if self.action == 0:   # 0: 打上补丁
				self.patch(0)
			elif self.action == 1: # 1：去除补丁
				self.patch(1)
			elif self.action == 2: # 2：生成补丁
				self.patch_new()

			# 切回路径
			path.pop()

		return

## patch对象.
patch = patch()
