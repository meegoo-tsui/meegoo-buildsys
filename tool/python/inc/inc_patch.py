#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    inc_patch.py
#  @brief   依据ini配置文件执行源码路径的相关补丁操作。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/09

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from   inc_printf   import printf

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 依据ini配置文件执行源码路径的相关补丁操作。
class patch:
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	## The constructor.
	def __init__(self):
		## 源码路径
		self.in_path    = ""
		## 补丁路径
		self.out_path   = ""
		## 补丁动作 - 0: 打上补丁，1：去除补丁，2：生成补丁
		self.action     = 0

## patch对象.
patch = patch()

