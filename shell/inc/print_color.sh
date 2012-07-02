#!/bin/bash
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ print_color.sh
#+   printf text with color
#+ author
#+   meegoo.tsui@gmail.com, 2012-06-28
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
txtrst=$(tput sgr0   ) # reset
txtred=$(tput setaf 1) # red
txtgrn=$(tput setaf 2) # green
txtylw=$(tput setaf 3) # yellow
txtblu=$(tput setaf 4) # blue
txtpur=$(tput setaf 5) # purple
txtcyn=$(tput setaf 6) # cyan
txtwht=$(tput setaf 7) # white

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
function print_help() 
{ 
	echo "${txtgrn}usage:${txtrst}"
	echo "${txtred}  print_color.sh -r "printf color - red"   ${txtrst}"
	echo "${txtgrn}  print_color.sh -g "printf color - green" ${txtrst}"
	echo "${txtylw}  print_color.sh -y "printf color - yellow"${txtrst}"
	echo "${txtblu}  print_color.sh -b "printf color - blue"  ${txtrst}"
	echo "${txtpur}  print_color.sh -p "printf color - purple"${txtrst}"
	echo "${txtcyn}  print_color.sh -c "printf color - cyan"  ${txtrst}"
	echo "${txtwht}  print_color.sh -w "printf color - white" ${txtrst}"
}

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# global vars
color=$txtrst
comment=""

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# getopt
args=`getopt -o r:g:y:b:p:c:w:h -l help -- "$@"`
if [ $? -ne 0 ];then
	echo "${txtred}args error, try -h or --help${txtrst}"
	exit 1
fi
eval set -- $args

for i;do
	case $i in
		-r) color=$txtred;comment=$2;shift 2;;
		-g) color=$txtgrn;comment=$2;shift 2;;
		-y) color=$txtylw;comment=$2;shift 2;;
		-b) color=$txtblu;comment=$2;shift 2;;
		-p) color=$txtpur;comment=$2;shift 2;;
		-c) color=$txtcyn;comment=$2;shift 2;;
		-w) color=$txtwht;comment=$2;shift 2;;	
		-h|--help)print_help;exit 0;;
		--)shift;;
	esac
done

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
echo "${color}$comment${txtrst}"

