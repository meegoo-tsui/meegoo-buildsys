#!/bin/sh
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# config env for build
#   meegoo tsui, 2012-09-04
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
TBSBIN=$HOME/.tbsbin
TOOLCHAINS=$HOME/workspace/toolchains
echo "解决工具不兼容问题"
if [ ! -d $TBSBIN ]; then
	mkdir -p $TBSBIN 
fi

$BUILD_SYS_PATH/tool/shell/print_color.sh -y "软链接 - automake"
ln -s $TOOLCHAINS/automake/automake-1.4/bin/automake $TBSBIN/automake-1.4
ln -s $TOOLCHAINS/automake/automake-1.5/bin/automake $TBSBIN/automake-1.5
ln -s $TOOLCHAINS/automake/automake-1.6/bin/automake $TBSBIN/automake-1.6
ln -s $TOOLCHAINS/automake/automake-1.7/bin/automake $TBSBIN/automake-1.7
ln -s $TOOLCHAINS/automake/automake-1.8/bin/automake $TBSBIN/automake-1.8
ln -s $TOOLCHAINS/automake/automake-1.9/bin/automake $TBSBIN/automake-1.9

$BUILD_SYS_PATH/tool/shell/print_color.sh -y "软链接 - gcc"
ln -s $TOOLCHAINS/gcc/gcc-4.1.1/bin/gcc $TBSBIN/gcc
ln -s $TOOLCHAINS/gcc/gcc-4.1.1/bin/g++ $TBSBIN/g++
ln -s $TOOLCHAINS/gcc/gcc-4.1.1/bin/gcc $TBSBIN/cc

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
export PATH="$TBSBIN:$PATH"
$BUILD_SYS_PATH/tool/shell/print_color.sh -y "PATH ="
$BUILD_SYS_PATH/tool/shell/print_color.sh -g "$PATH"

