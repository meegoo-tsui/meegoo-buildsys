#! /usr/bin/python

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    inc_ini.py
#  @brief   ini file parser.
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys
import ConfigParser

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   inc_printf   import printf

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## ini file parser.
class ini:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## default input ini file.
		self.build_ini       = "build.ini"

		## patser for build.ini
		self.build_configIni = ConfigParser.ConfigParser()

		## build path: source, makefile, patch and install.
		self.build_paths     = [
		                        ("source.path",""), 
		                        ("makefile.path",""), 
		                        ("patch.path",""), 
		                        ("install.path","")
		                       ]

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
					if os.path.isdir(temp_path):
						printf.silence("\t" + j[0] + " - " + temp_path)
					else:
						printf.error(temp_path + " is not a diretory !")
				else:
					printf.silence("\t" + j[0] + " - no")
		return

## object of class ini.
ini = ini()

