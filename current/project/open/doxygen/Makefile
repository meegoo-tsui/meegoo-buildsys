#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Makefile:
#+   doxygen
#+ author:
#+   meegoo.tsui@gmail.com
#+ date:
#+   2012/07/11
#+
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
include buildsys.mak

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 源码位置
DOXYGEN_PATH   = $(HOME)/workspace/open/svn/doxygen

# 安装路径
PREFIX         = $(EXEC_DIR)

# 配置标志文件
CONFIG_TOUCH   = config.touch
# 配置日志
CONFIG_LOG     = $(PWD)/configure.log
# 编译日志
MAKE_LOG       = $(PWD)/make.log

# 配置选项
DOXYGEN_CONFIG = ./configure --with-doxywizard

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
all: copy config
	@set -e; \
	if [ -d $(SRC_DIR) ]; then \
		cd $(SRC_DIR); \
		make all 2>$(MAKE_LOG); \
	fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
clean: copy config
	@set -e; \
	if [ -d $(SRC_DIR) ]; then \
		cd $(SRC_DIR); \
		make clean; \
	fi
	@rm -f buildsys.mak *.log

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
install: 
	@set -e; \
	if [ -d $(SRC_DIR) ]; then \
		cd $(SRC_DIR); \
		sudo make install; \
	fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
copy:
	@set -e; \
	if [ ! -d $(DOXYGEN_PATH) ]; then \
		echo "checkout doxygen ..."; \
		svn co https://doxygen.svn.sourceforge.net/svnroot/doxygen/trunk $(DOXYGEN_PATH); \
	fi; \
	if [ ! -d $(SRC_DIR) ]; then \
		echo "复制doxygen源码..."; \
		links.py -s $(DOXYGEN_PATH) -d $(SRC_DIR); \
	fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
config:
	@set -e; \
	cd $(SRC_DIR); \
	if [ ! -f $(CONFIG_TOUCH) ]; then \
		echo $(CONFIG_TOUCH); \
		$(DOXYGEN_CONFIG) 2>$(CONFIG_LOG); \
		touch $(CONFIG_TOUCH); \
	fi

