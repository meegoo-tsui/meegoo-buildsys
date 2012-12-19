#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    arg.py
#  @brief   所有工具的参数解析及帮助信息。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import sys
import getopt

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf   import printf

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 参数解析、帮助信息。
class arg:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具build.py的帮助信息。
	def build_usage(self):
		printf.printf(3, "Usage:\n" + "build.py " + "[options]")
		printf.printf(3, '''
Options:
-h | --help  print help info
-c           make clean
-m           make
-i           make install
-x           make others,此参数只能唯一存在
default      make clean, make, make install
''')

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具build.py的解析参数。
	def build_args(self):
		printf.status("parse args ...")
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hcmix:", ["help"])
		except getopt.GetoptError , err:
			printf.warn(str(err)) # will print something like "option -a not recognized"
			self.build_usage()
			sys.exit(1)

		## build参数字典
		build_args = {'-c':0, '-m':0, '-i':0, '-x':''} # 默认为非法参数
		for o, a in opts:
			if   o in ("-h", "--help"):
				self.build_usage()
				sys.exit(1)
			elif o == "-c":
				build_args[o] = 1
			elif o == "-m":
				build_args[o] = 1
			elif o == "-i":
				build_args[o] = 1
			elif o == "-x":
				build_args[o] = ' '.join(str(n) for n in sys.argv[2:])
			else:
				assert False, "unhandled option"
				self.build_usage()
				sys.exit(1)

		return build_args

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具patch.py的帮助信息。
	def patch_usage(self):
		printf.printf(3, "Usage:\n" + "patch.py " + "[options]")
		printf.printf(3, '''
Options:
-h | --help  print help info
-f           ini file path
-a           action:
             0 - do patch
             1 - undo patch
             2 - create patch
-u           patch for untrack files, default without it
''')

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具patch.py的解析参数。
	def patch_args(self):
		printf.status("parse args ...")
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hf:a:u", ["help"])
		except getopt.GetoptError , err:
			printf.warn(str(err)) # will print something like "option -a not recognized"
			self.patch_usage()
			sys.exit(1)

		## patch参数字典，ini路径、patch动作
		patch_args = {'-f':'', '-a':-1, '-u':0} # 默认为非法参数
		for o, a in opts:
			if   o in ("-h", "--help"):
				self.patch_usage()
				sys.exit(1)
			elif o == "-f":
				patch_args[o] = a
			elif o == "-a":
				patch_args[o] = int(a)
			elif o == "-u":
				patch_args[o] = 1 # 需要对非托管文件打补丁
			else:
				assert False, "unhandled option"
				self.patch_usage()
				sys.exit(1)

		# 判断参数
		if patch_args['-a'] < 0 or patch_args['-f'] == "":
			self.patch_usage()
			sys.exit(1)

		return patch_args

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具check.py的帮助信息。
	def check_usage(self):
		printf.printf(3, "Usage:\n" + "check.py " + "[options]")
		printf.printf(3, '''
Options:
-h | --help  print help info
-f           ini file path
-l           list all repos
-o           checkout the repos
''')

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具check.py的解析参数。
	def check_args(self):
		printf.status("parse args ...")
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hf:lo:", ["help"])
		except getopt.GetoptError , err:
			printf.warn(str(err)) # will print something like "option -a not recognized"
			self.check_usage()
			sys.exit(1)

		## check参数字典，ini路径
		check_args = {'-f':'', '-l':'' , '-o':''} # 默认为非法参数
		for o, a in opts:
			if   o in ("-h", "--help"):
				self.check_usage()
				sys.exit(1)
			elif o == "-f":
				check_args[o] = a
			elif o == "-l":
				check_args[o] = "true"
			elif o == "-o":
				check_args[o] = a
			else:
				assert False, "unhandled option"
				self.check_usage()
				sys.exit(1)

		# 判断参数
		if check_args['-f'] == "":
			self.check_usage()
			sys.exit(1)

		return check_args

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具svn.py或git.py的帮助信息。
	def repos_usage(self, repos):
		printf.printf(3, "Usage:\n" + repos + ".py " + "[options]")
		printf.printf(3, '''
Options:
-h | --help  print help info
-m           list modify files
-d           list delete files
-o           list others files
-c           clean all repos at current path
-b           backup all repost
-s           repos status
''')

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具svn.py或git.py的解析参数。
	def repos_args(self, repos):
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hmdocbs", ["help"])
		except getopt.GetoptError , err:
			printf.warn(str(err)) # will print something like "option -a not recognized"
			self.repos_usage()
			sys.exit(1)

		## svn.py或git.py
		repos_args = ""
		for o, a in opts:
			if   o in ("-h", "--help"):
				self.repos_usage(repos)
				sys.exit(1)
			else:
				repos_args = o

		return repos_args

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具links.py的帮助信息。
	def links_usage(self):
		printf.printf(3, "Usage:\n" + "links.py " + "[options]")
		printf.printf(3, '''
Options:
-h | --help  print help info
-s           source folder
-d           link folder
''')

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## 工具links.py的解析参数。
	def links_args(self):
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hs:d:", ["help"])
		except getopt.GetoptError , err:
			printf.warn(str(err)) # will print something like "option -a not recognized"
			self.links_usage()
			sys.exit(1)

		links_args = {'-s':'', '-d':''} # 默认为非法参数
		for o, a in opts:
			if   o in ("-h", "--help"):
				self.links_usage()
				sys.exit(1)
			else:
				links_args[o] = a
		return links_args

## arg对象。
arg = arg()
