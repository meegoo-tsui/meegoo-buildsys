#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Makefile:
#+   libdaemon
#+ author:
#+   meegoo.tsui@gmail.com
#+ date:
#+   2012/07/11
#+ http://0pointer.de/lennart/projects/libdaemon/
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
include buildsys.mak

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 源码位置
REPOS_LOCAL      = $(HOME)/workspace/open/git/$(PROJECT)
# 安装路径
PREFIX           = $(EXEC_DIR)
# 配置标志文件
CONFIG_TOUCH     = config.touch
# 配置日志
CONFIG_LOG       = $(PWD)/configure.log
# 编译日志
MAKE_LOG         = $(PWD)/make.log
# 配置选项
BUILD_CONFIG     = 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
all: copy config
	@echo "all - need continue ..."

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
clean: copy config
	@echo "clean - need continue ..."
	@rm -f buildsys.mak *.log

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
install:
	@echo "install - need continue ..."

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
copy:
	@set -e; \
 	if [ ! -d $(REPOS_LOCAL) ]; then \
		echo "checkout $(PROJECT) ..."; \
		git clone $(REPOS) $(REPOS_LOCAL); \
	fi; \
	if [ ! -d $(SRC_DIR) ]; then \
		mkdir -p $(SRC_DIR); \
	fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
config:
	@echo "config - need continue ..."

