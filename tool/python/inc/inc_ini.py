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

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 解析各种ini配置文件。
class ini:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## default input ini file.
		self.build_ini       = "build.ini"

		## patser for build.ini
		self.build_configIni = ConfigParser.ConfigParser()
		
		## current section pos
		self.section_current = ""

		## build path: source, makefile, patch and install.
		self.build_paths     = [
		("makefile.path",""),
		("install.path",""),
		("source.path",""),  
		("patch.path","")]

		## makefile.path在字典self.build_paths中位置
		self.pos_makefile = 0
		
		## install.path在字典self.build_paths中位置
		self.pos_install  = 1
		
		## source.path在字典self.build_paths中位置
		self.pos_source   = 2
		
		## patch.path在字典self.build_paths中位置
		self.pos_patch    = 3

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## parser of build.ini
	def build_parse(self):
		# judge build_ini exists
		printf.status("parse ini ...")
		self.build_ini = os.getcwd() + "/" + self.build_ini
		if not os.path.exists(self.build_ini):
			printf.error(self.build_ini + " is not exsit !")
			sys.exit(1)

		# parse build_ini
		fp = open(self.build_ini,"r")
		self.build_configIni.readfp(fp)
		fp.close()
		# parse all sections
		for i in sorted(self.build_configIni.sections()):
			printf.silence("project: " + i)
			for j in self.build_paths:
				if self.build_configIni.has_option(i, j[0]):
					temp_path = os.path.expandvars(self.build_configIni.get(i, j[0]))
					printf.silence("\t" + j[0] + " - " + temp_path)				
					if not os.path.isdir(temp_path):
						if j[0] == self.build_paths[self.pos_makefile][0]: # only check Makefile path
							printf.error(temp_path + " is not a diretory !")							
				else:
					printf.silence("\t" + j[0] + " - no")
		return

## object of class ini.
ini = ini()
