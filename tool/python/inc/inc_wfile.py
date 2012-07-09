#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    inc_wfile.py
#  @brief   依据ini配置文件生成其他编译辅助文件。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   inc_printf   import printf
from   inc_ini      import ini

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
	def wmakefile(self):
		makefile_path = os.path.expandvars(ini.build_configIni.get(ini.section_current, ini.build_paths[ini.pos_makefile][0]))
		fp = open(makefile_path + "/" + self.makefile,'w')
		# 添加安装路径到makefile
		if ini.build_configIni.has_option(ini.section_current, ini.build_paths[ini.pos_install][0]):
			install_path  = os.path.expandvars(ini.build_configIni.get(ini.section_current, ini.build_paths[ini.pos_install][0]))
			fp.write("# 安装路径\n" + "EXEC_DIR = " + install_path + "\n")
		# 添加源码路径到makefile
		if ini.build_configIni.has_option(ini.section_current, ini.build_paths[ini.pos_source][0]):
			install_path  = os.path.expandvars(ini.build_configIni.get(ini.section_current, ini.build_paths[ini.pos_source][0]))
			fp.write("# 源码路径\n" + "SRC_DIR = " + install_path + "\n")
		fp.close()
		return

## wfile对象.
wfile = wfile()
