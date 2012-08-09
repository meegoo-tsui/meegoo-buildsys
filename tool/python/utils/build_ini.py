#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    build_ini.py
#  @brief   解析build.ini配置文件。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys
import ConfigParser

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf   import printf
from   utils.glb      import glb

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 解析各种ini配置文件。
class build_ini:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## default input ini file.
		self.ini       = ""

		## parser for build.ini
		self.configIni = ConfigParser.ConfigParser()

		## 字典列表，每个section对应一个字典
		self.list_of_dict    = []

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## parser of ini file
	def parse(self, ini):
		# judge ini exists
		printf.status("parse ini ...")
		self.ini = ini
		if not os.path.exists(self.ini):
			printf.error(self.ini + " is not exsit !")
			sys.exit(1)

		# parse ini
		fp = open(self.ini,"r")
		self.configIni.readfp(fp)
		fp.close()

		# parse all sections
		for i in sorted(self.configIni.sections()):
			## 初始化字典	
			dictionary = {}
			dictionary[glb.project_name] = i

			## 读取所有option到字典
			for j in self.configIni.options(i):
				dictionary[j] = os.path.expandvars(self.configIni.get(i, j))
			self.list_of_dict.append(dictionary)

		## 打印解析到的数据
		for i in self.list_of_dict:
			printf.silence("\nsection:")
			for key in i.keys():
				printf.silence(key + " = " + i[key])

		return

## object of class ini.
build_ini = build_ini()
