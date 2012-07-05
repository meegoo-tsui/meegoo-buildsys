#! /usr/bin/python

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    buildsys_import.py
#  @brief   buildsys import.
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## buildsys import path
buildsys_import_path = os.environ["BUILD_SYS_PATH"] + "/python"
## all import folders
import_folder        = sorted(os.listdir(buildsys_import_path))

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Add path to python system path
for i in import_folder:
	## new system path for python
	sys_path = buildsys_import_path + "/" + i
	if os.path.isdir(sys_path):
		if sys_path not in sys.path:
			sys.path.insert(0, sys_path)

