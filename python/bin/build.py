#! /usr/bin/python

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    build.py
#  @brief   build projects via build.ini.
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys
import ConfigParser

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## buildsys import path
buildsys_import_path = os.environ["BUILD_SYS_PATH"] + "/python"
if buildsys_import_path not in sys.path:
     sys.path.insert(0, buildsys_import_path)
import buildsys_import

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from inc_printf import printf
from inc_time   import time
from inc_path   import path
from inc_cmd    import cmd
from inc_arg    import arg
from inc_make   import make

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## build tool for all project.
class build:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## default input ini file.
		self.build_ini  = "build.ini"

		## default build action, 0 - build all, 1 - make clean, 2 - make, 3 - make install.
		self.build_type = 0

		## patser for build.ini
		self.ConfigIni      = ConfigParser.ConfigParser()

		## build path: source, makefile, patch and install.
		self.path = [
		             ("source.path",""), 
		             ("makefile.path",""), 
		             ("patch.path",""), 
		             ("install.path","")
		            ]

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## parse ini file
	def ini(self):
		# judge build_ini exists
		printf.status("parse ini ...")
		self.build_ini = os.getcwd() + "/" + self.build_ini
		if not os.path.exists(self.build_ini):
			printf.error(self.build_ini + " is not exsit !")
			sys.exit(1)

		# parse build_ini
		self.ConfigIni = ConfigParser.ConfigParser()
		fp = open(self.build_ini,"r")
		self.ConfigIni.readfp(fp)
		fp.close()
		# parse all sections
		for i in sorted(self.ConfigIni.sections()):
			printf.silence("project: " + i)
			for j in self.path:
				if self.ConfigIni.has_option(i, j[0]):
					temp_path = os.path.expandvars(self.ConfigIni.get(i, j[0]))
					if os.path.isdir(temp_path):
						printf.silence("\t" + j[0] + " - " + temp_path)
					else:
						printf.error(temp_path + " is not a diretory !")
				else:
					printf.silence("\t" + j[0] + " - no")
		return

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## build action
	def build(self):
		printf.status("build ...")
		# build all projects
		for i in sorted(self.ConfigIni.sections()):
			printf.silence("build project: " + i)
			temp_path = os.path.expandvars(self.ConfigIni.get(i, self.path[1][0]))
			path.push()
			path.change(temp_path)
			if self.build_type == 1:
				make.makeclean()
			elif self.build_type == 2:
				make.make()
				make.makeinstall()
			elif self.build_type == 3:
				make.makeinstall()
			else:
				make.makeclean()
				make.make()
				make.makeinstall()
			path.pop()

		return

## object of class build
build = build()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## main function.
def main():
	
	# start build
	printf.reset()
	time.push(os.path.abspath(__file__))

	# build the project
	build.build_type = arg.build_args()
	build.ini()
	build.build()

	# end build
	time.pop()
	printf.silence("all done.")
	sys.exit(0)

if __name__ == '__main__':
	main()

