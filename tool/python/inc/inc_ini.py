#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    inc_ini.py
#  @brief   解析各种ini配置文件。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys
import ConfigParser

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   inc_printf   import printf
from   inc_glb      import glb

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 解析各种ini配置文件。
class ini:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## default input ini file.
		self.build_ini       = ""

		## parser for build.ini
		self.build_configIni = ConfigParser.ConfigParser()

		## 字典列表，每个section对应一个字典
		self.list_of_dict    = []

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## parser of build.ini
	def build_parse(self, build_ini):
		# judge build_ini exists
		printf.status("parse ini ...")
		self.build_ini = build_ini
		if not os.path.exists(self.build_ini):
			printf.error(self.build_ini + " is not exsit !")
			sys.exit(1)

		# parse build_ini
		fp = open(self.build_ini,"r")
		self.build_configIni.readfp(fp)
		fp.close()

		# parse all sections
		for i in sorted(self.build_configIni.sections()):
			## 初始化字典	
			dictionary = {}
			dictionary[glb.project_name] = i

			## 读取所有option到字典
			for j in self.build_configIni.options(i):
				dictionary[j] = os.path.expandvars(self.build_configIni.get(i, j))
			self.list_of_dict.append(dictionary)

		## 打印解析到的数据
		for i in self.list_of_dict:
			printf.silence("\nsection:")
			for key in i.keys():
				printf.silence(key + " = " + i[key])

		return

## object of class ini.
ini = ini()
