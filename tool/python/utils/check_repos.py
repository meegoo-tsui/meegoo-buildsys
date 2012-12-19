#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    check_repos.py
#  @brief   依据ini配置文件执行源码的check out。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/09

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys
import ConfigParser

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   utils.printf         import printf
from   utils.cmd            import cmd
from   utils.path           import path

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 依据ini配置文件执行源码的check out。
class check_repos:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## check 参数字典
		self.check_args = {}

		## default input ini file.
		self.ini        = ""

		## parser for repos.ini
		self.configIni = ConfigParser.ConfigParser()

		## 字典{"name":["path", "action"]
		self.dict      = {}

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## check out source code
	def check_out(self, ini):
		self.ini = ini
		printf.status("parse ini ...")
		if not os.path.exists(self.ini):
			printf.error(self.ini + " is not exsit !")
			sys.exit(1)

		# read ini
		fp = open(self.ini,"r")
		self.configIni.readfp(fp)
		fp.close()

		# parse all sections
		for opts in self.configIni.options("repos"):
			# name
			i = opts.split(".")[0]
			# path
			j = os.path.expandvars(self.configIni.get("path", i + ".path"))
			# repos
			k = self.configIni.get("repos", opts)
			self.dict[i] = [j, k]

		# print check info
		cnt = 0
		chk_one_flg = 0
		printf.status("repos status ...")
		for i in sorted(self.dict):
			if self.check_args['-o'] != "":
				if self.check_args['-o'] == i:
					chk_one_flg = 1
					break
				else:
					continue
			cnt = cnt + 1
			printf.silence(str(cnt) + " - " + i)
			repos_path = self.dict[i][0] + "/" + i
			printf.silence("path - " + repos_path)										
			if os.path.isdir(repos_path):
				printf.silence("action - update\n")
			else:
				printf.silence("action - " + self.dict[i][0] + "\n")

		# olny list all repos name
		if self.check_args['-l'] != "":
			return 0

		# judge check one
		if self.check_args['-o'] != "" and chk_one_flg == 0:
			printf.error("No <" + self.check_args['-o'] + "> @ " + self.ini)

		# check out or update
		cnt = 0
		printf.status("check out or update ...")
		for i in sorted(self.dict):
			if chk_one_flg == 1:
				if self.check_args['-o'] != i:
					continue
			cnt = cnt + 1
			printf.silence(str(cnt) + " - " + i)
			repos_path = self.dict[i][0] + "/" + i
			if os.path.isdir(repos_path):
				printf.silence("action - update\n")
				path.push()
				path.change(repos_path)
				if self.dict[i][1].find("git clone") != -1:
					printf.silence("git repos")
					cmd.do("git reset --hard")
					cmd.do("git pull")
				elif self.dict[i][1].find("svn co") != -1:
					printf.silence("svn repos")
					cmd.do("svn up")
				else:
					printf.warn("unkown - " + self.dict[i][1])
				path.pop()
			else:
				cmd.do("mkdir -p " + self.dict[i][0])
				path.push()
				path.change(self.dict[i][0])
				cmd.do(self.dict[i][1])
				path.pop()

## patch对象.
check_repos = check_repos()
