#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    inc_wfile.py
#  @brief   依据ini配置文件生成其他编译辅助文件。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   inc_printf   import printf
from   inc_glb      import glb

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

		# 添加安装路径到makefile
		if project_dict.has_key(glb.installe_path):
			fp.write("# 安装路径\n" + "EXEC_DIR = " + project_dict[glb.installe_path] + "\n")
		
		# 添加源码路径到makefile
		if project_dict.has_key(glb.source_path):
			fp.write("# 源码路径\n" + "SRC_DIR = " + project_dict[glb.source_path] + "\n")

		# 写文件完成
		fp.close()

		return

## wfile对象.
wfile = wfile()
