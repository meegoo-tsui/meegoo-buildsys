#!/bin/bash
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ buildsys_env.sh
#+   config buildsys env
#+ usage:
#+   . buildsys_env.sh
#+ author
#+   meegoo.tsui@gmail.com, 2012-06-28
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if [ "$BUILD_SYS_ENV" == "" ]; then
	export BUILD_SYS_ENV=OK
	export BUILD_SYS_PATH=$PWD
	$BUILD_SYS_PATH/shell/inc/print_color.sh -y "[Set buildsys path]:"
	$BUILD_SYS_PATH/shell/inc/print_color.sh -g "BUILD_SYS_PATH = $BUILD_SYS_PATH"
	
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	export PATH="$BUILD_SYS_PATH/shell/inc:$PATH"
	export PATH="$BUILD_SYS_PATH/shell/bin:$PATH"
	export PATH="$BUILD_SYS_PATH/python/inc:$PATH"
	export PATH="$BUILD_SYS_PATH/python/bin:$PATH"
	$BUILD_SYS_PATH/shell/inc/print_color.sh -y "[Add User tools to path]:"
	$BUILD_SYS_PATH/shell/inc/print_color.sh -g "PATH = $PATH"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
else
	$BUILD_SYS_PATH/shell/inc/print_color.sh -y "config env is done."
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

