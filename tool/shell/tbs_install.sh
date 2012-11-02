#!/bin/sh
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# config env for build
#   meegoo tsui, 2012-09-04
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 得到主机版本
ARCH=$(uname -m | sed 's/x86_//;s/i[3-6]86/32/')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
$BUILD_SYS_PATH/tool/shell/print_color.sh -y "安装相关软件 ..."
sudo apt-get install libncurses5-dev libexpat-dev libattr1-dev libpng12-dev
sudo apt-get install autoconf bison flex gawk sharutils ctags

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
$BUILD_SYS_PATH/tool/shell/print_color.sh -y "解决权限问题"
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

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
$BUILD_SYS_PATH/tool/shell/print_color.sh -y "解决lib包含问题问题"
sudo ln -s /usr/lib/i386-linux-gnu/libcrypt.a    /usr/lib/libcrypt.a 
sudo ln -s /usr/lib/i386-linux-gnu/libcrypt.so   /usr/lib/libcrypt.so 
sudo ln -s /usr/lib/i386-linux-gnu/libncurses.a  /usr/lib/libncurses.a 
sudo ln -s /usr/lib/i386-linux-gnu/libncurses.so /usr/lib/libncurses.so

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
$BUILD_SYS_PATH/tool/shell/print_color.sh -g "安装相关软件完成"

