#!/bin/sh
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# config env for build
#   meegoo tsui, 2012-09-04
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 需要安装包:
# subversion git flex g++ gawk zlib1g-dev libncurses5-dev
# libncurses5-dev libncursesw5-dev
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 得到主机版本
ARCH=$(uname -m | sed 's/x86_//;s/i[3-6]86/32/')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 解决 -lcrypt 包含问题问题
if [ "$ARCH" -eq "32" ]; then
	echo "host - x86 32"
	if [ ! -f /usr/lib/libcrypt.a ]; then
		sudo ln -s /usr/lib/i386-linux-gnu/libcrypt.a /usr/lib/libcrypt.a
	fi
	if [ ! -f /usr/lib/libcrypt.so ]; then
		sudo ln -s /usr/lib/i386-linux-gnu/libcrypt.so /usr/lib/libcrypt.so
	fi
else
	echo "host - x86 64"
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 解决权限问题
if [ `whoami` == "root" -o -u `which chmod` ];then
	echo "check chmod ok ..."
else
	sudo chmod u+s /bin/chmod
fi
if [ `whoami` == "root" -o -u `which mknod` ];then
	echo "check mknod ok ..."
else
	sudo chmod u+s /bin/mknod
fi

