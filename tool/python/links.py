#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    src_links.py
#  @brief   编译工具，创建源码软链接。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/10/20

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.time           import time
from   utils.arg            import arg
from   utils.cmd            import cmd

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## main function.
def main():
	# start links
	printf.reset()
	time.push(os.path.abspath(__file__))
	links_args = arg.links_args()
	
	# Judge source folder
	if not os.path.isdir(links_args['-s']):
		printf.error("No a dir - " + links_args['-s'])
	if not os.path.isdir(links_args['-d']):
		cmd.do("mkdir -p " + links_args['-d'])
	links_args['-s'] = os.path.abspath(links_args['-s'])

	# create folder and link for file
	printf.status("links ...")
	for root, dirs, files in os.walk(links_args['-s']):		
		# set filter
		if '.git' in dirs:
			dirs.remove('.git')  # don't visit .git directories
		if '.svn' in dirs:
			dirs.remove('.svn')  # don't visit .svn directories

		# Create folder
		current_folder = root.replace(links_args['-s'], "")
		new_folder     = links_args['-d'] + "/" + current_folder
		cmd_mkdir = "mkdir -p " + "\"" + new_folder + "\""
		os.system(cmd_mkdir)
		sys.stdout.write('\r' + current_folder)
		sys.stdout.flush()
		#print "\r\n", cmd_mkdir
		#raw_input("Press ENTER to exit")

		# link for files
		for f in files:
			source_file = "\"" + root       + "/" + f + "\""
			link_file   = "\"" + new_folder + "/" + f + "\""
			cmd_ln = "ln -sf " + source_file + " " + link_file
			os.system(cmd_ln)
			#print "\r\n", cmd_ln
		size = len(current_folder)
		sys.stdout.write('\r' + ' '*size)
		sys.stdout.flush()

	# done.
	print ""
	printf.status("links done.")

	# end links
	time.pop()
	sys.exit(0)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if __name__ == '__main__':
	main()
