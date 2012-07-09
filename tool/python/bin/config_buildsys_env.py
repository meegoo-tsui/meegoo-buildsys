#! /usr/bin/python
#coding=utf-8

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    config_buildsys_env.py
#  @brief   环境工具，修改$HOME/.bashrc，自动设置环境变量。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/05

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, sys

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## buildsys import path
buildsys_import_path = os.environ["BUILD_SYS_PATH"] + "/tool/python"
if buildsys_import_path not in sys.path:
     sys.path.insert(0, buildsys_import_path)
import buildsys_import

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from inc_printf import printf

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## .bashrc文件路径。
bashrc_file = os.path.expandvars("$HOME/.bashrc")
## 修改标志字符串。
config_flag = "# Configure buildsys ENV"
## 添加内容。
env_content = "#"*80 + "\n" + config_flag + \
'''
current_path=$PWD
cd $HOME/git/meegoo-buildsys/env
. .env
cd $current_path

'''

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 主函数。
def main():
	printf.reset()

	# judge config
	fp = open(bashrc_file,"r")
	for line in fp:
		if config_flag in line:
			fp.close()
			printf.status("Config env for buildsys already.")
			sys.exit(0)
	fp.close()

	# modify .bashrc
	fp = open(bashrc_file,"a")
	fp.write(env_content)
	fp.close()
	printf.status("Config env for buildsys success.")

	sys.exit(0)
if __name__ == '__main__':
	main()

