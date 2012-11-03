#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    wfile.py
#  @brief   依据ini配置文件生成其他编译辅助文件。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf   import printf
from   utils.glb      import glb

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 依据ini配置文件生成其他编译辅助文件。
class wfile:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## default makefile name
		self.makefile       = "buildsys.mak"

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 依据build.ini生成makefile包含文件。
	def wmakefile(self, project_dict):
		# 开始写文件
		printf.status("write include makefile ...")
		file_name = project_dict[glb.project_path] + "/" + self.makefile
		fp = open(file_name, 'w')
		printf.silence("file - " + file_name)

		# 添加项目名称到makefile
		if project_dict.has_key(glb.project_name):
			fp.write("# 项目名称\n" + "PROJECT = " + project_dict[glb.project_name] + "\n")

		# 添加源码路径到makefile
		if project_dict.has_key(glb.source_path):
			fp.write("# 源码路径\n" + "SRC_DIR = " + project_dict[glb.source_path] + "\n")

		# 添加安装路径到makefile
		if project_dict.has_key(glb.installe_path):
			fp.write("# 安装路径\n" + "EXEC_DIR = " + project_dict[glb.installe_path] + "\n")

		# 添加补丁路径到makefile
		if project_dict.has_key(glb.patch_path):
			fp.write("# 补丁路径\n" + "PATCH_DIR = " + project_dict[glb.patch_path] + "\n")
			fp.write("# 补丁标志\n" + "PATCH_FLAG = " + glb.patch_flag + "\n")

		# 添加开源路径到makefile
		if project_dict.has_key(glb.repos):
			fp.write("# 开源路径\n" + "REPOS = " + project_dict[glb.repos] + "\n")
		
		# 写文件完成
		fp.close()

		return

## wfile对象.
wfile = wfile()
