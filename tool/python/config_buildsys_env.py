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
from utils.printf   import printf

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## .bashrc文件路径。
bashrc_file = os.path.expandvars("$HOME/.bashrc")
## 修改标志字符串。
config_flag = "# Configure buildsys ENV"
## 添加内容。
BUILD_SYS_PATH = os.path.expandvars("$BUILD_SYS_PATH")
env_content = "#" + "+"*79 + "\n" + config_flag + "\n" + \
"BUILD_SYS_PATH="  + BUILD_SYS_PATH + \
'''
if [ -f $BUILD_SYS_PATH/tool/env/.env ] ; then
	current_path=$PWD
	cd $BUILD_SYS_PATH/tool/env
	. .env
	cd "$current_path"
fi
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
