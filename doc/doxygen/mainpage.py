## @mainpage 
#
# @authors meegoo.tsui@gmail.com
# @date    2012-07-05
#
# @section intro 简介
# 编译工具集，使用build.ini作为编译配置文件，传递各种在编译过程中需要的路径及选项。
# - 主要特点
# -# 编译分为make clean、make、make install；
# -# build.ini包含多个section，意味着一次可以自动编译多个项目；
# -# 提供补丁路径，编译前打好补丁，在工具集中提供补丁工具；
# -# 根据build.ini提供的选项，生成Makefile包含文件，灵活控制编译过程；
# -# 使用python脚本，功能强大及易于使用；
#
# - 使用方法
# -# 设置环境变量，cd tool/env; source .env
# -# 使用编译示例，cd open/qt/x11; build.py -h

