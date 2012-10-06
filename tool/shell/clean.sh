#!/bin/bash
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ clean.sh
#+   clean temp files and termenal
#+ author
#+   meegoo.tsui@gmail.com, 2012-06-28
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
current_path=$PWD      # 保存原始路径
exe_path=$current_path # 执行清理路径

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function clean_help() 
{ 
	echo -e "usage:"
	echo -e "\tclean.sh"
	echo -e "\tclean.sh -C $HOME"
	exit 1
}

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# getopt
args=`getopt -o C:h -l help -- "$@"`
eval set -- $args
for i;do
	case $i in
		-C) exe_path=$2;shift 2;;	
		-h|--help)clean_help;;
		--)shift;;
	esac
done

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
cd $exe_path
find . -iname "*.pyc"        | xargs rm -f # 删除当前路径的临时文件
find . -iname "*.log"        | xargs rm -f # 删除当前路径的临时文件
find . -iname "buildsys.mak" | xargs rm -f # 删除当前路径的临时文件
echo -e \\033c                             # 终端内容清除
cd $current_path                           # 路径恢复

