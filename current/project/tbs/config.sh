#!/bin/sh
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# config env for build
#   meegoo tsui, 2012-09-04
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 得到主机版本
ARCH=$(uname -m | sed 's/x86_//;s/i[3-6]86/32/')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# $(SRC_DIR)/RTL8676/RTL8676xx/src/opensource/ppp-pppoe/ppp-2.4.3/pppd/Makefile.linux - 123
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

