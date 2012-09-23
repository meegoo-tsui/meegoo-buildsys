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
SVN_PATH = $(HOME)/workspace/open/svn/doxygen-svn

# 安装路径
PREFIX       = $(EXEC_DIR)

# 编译日志
MAKE_LOG     = $(PWD)/make.log

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
all: copy config
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
		if [ -f Makefile ]; then \
			make clean; \
			rm -f Makefile; \
		fi; \
		svn status | grep "^?" | awk '{print $2}' | xargs rm -rf; \
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
	if [ ! -d $(SVN_PATH) ]; then \
		echo "checkout doxygen ..."; \
		svn co https://doxygen.svn.sourceforge.net/svnroot/doxygen/trunk $(SVN_PATH); \
	fi; \
	if [ ! -d $(SRC_DIR) ]; then \
		echo "复制doxygen源码..."; \
		cp -r $(SVN_PATH) $(SRC_DIR); \
	fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
config:
	@set -e; \
	cd $(SRC_DIR); \
	./configure --prefix $(PREFIX) --with-doxywizard 

