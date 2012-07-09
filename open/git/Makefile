#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Makefile:
#+   git
#+ author:
#+   meegoo.tsui@gmail.com
#+ date:
#+   2012/07/09
#+
#+ 依赖包：
#+   1. sudo apt-cache search "libcurl*"
#+   2. sudo apt-get install libcurl4-gnutls-dev
#+
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
include buildsys.mak

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# git 源码位置
GIT_PATH   = $(HOME)/git/open/git
# git 版本
VER        = v1.7.9.7
# 安装路径
PREFIX     = $(EXEC_DIR)/$(VER)
# Qt 编译日志
MAKE_LOG   = $(PWD)/make.log

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
all: copy
	@set -e; \
	if [ -d $(SRC_DIR) ]; then \
		cd $(SRC_DIR); \
		make prefix=$(PREFIX) all 2>$(MAKE_LOG); \
	fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
clean: 
	@set -e; \
	if [ -d $(SRC_DIR) ]; then \
		cd $(SRC_DIR); \
		git reset --hard; \
		git clean -fdx; \
		git checkout $(VER); \
		make clean; \
	fi
	@rm -f buildsys.mak $(MAKE_LOG)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
install: 
	@set -e; \
	if [ -d $(SRC_DIR) ]; then \
		cd $(SRC_DIR); \
		sudo make prefix=$(PREFIX) install; \
	fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
copy:
	@set -e; \
	if [ ! -d $(QT_GIT_PATH) ]; then \
		echo "克隆git源码..."; \
		git clone git://git.kernel.org/pub/scm/git/git.git $(GIT_PATH); \
	fi; \
	if [ ! -d $(SRC_DIR) ]; then \
		echo "复制git源码..."; \
		cp -r $(GIT_PATH) $(SRC_DIR); \
	fi

