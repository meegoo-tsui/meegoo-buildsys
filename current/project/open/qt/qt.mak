#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ qt.mak:
#+   Qt build include
#+ author:
#+   meegoo.tsui@gmail.com
#+ date:
#+   2012/07/09
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Qt 源码位置
QT_GIT_PATH   = $(HOME)/workspace/open/git/qt
# Qt 配置标志文件
CONFIG_TOUCH  = config.touch
# Qt 配置日志
CONFIG_LOG    = $(PWD)/configure.log
# Qt 编译日志
MAKE_LOG      = $(PWD)/make.log

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
all_base: copy config
	@set -e; \
	cd $(SRC_DIR); \
	make 2>$(MAKE_LOG)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
clean_base:
	@set -e; \
	if [ -d $(SRC_DIR) ]; then \
		cd $(SRC_DIR); \
		if [ -f $(CONFIG_TOUCH) ]; then \
			make confclean; \
			rm -f $(CONFIG_TOUCH); \
		fi; \
	fi
	@rm -f buildsys.mak $(CONFIG_LOG) $(MAKE_LOG)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
install_base: 
	@set -e; \
	cd $(SRC_DIR); \
	sudo make install

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
copy:
	@set -e; \
	if [ ! -d $(QT_GIT_PATH) ]; then \
		echo "克隆Qt源码..."; \
		git clone git://gitorious.org/qt/qt.git $(QT_GIT_PATH); \
	fi; \
	if [ ! -d $(SRC_DIR) ]; then \
		mkdir -p $(SRC_DIR); \
	fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
config:
	@set -e; \
	cd $(SRC_DIR); \
	if [ ! -f $(CONFIG_TOUCH) ]; then \
		echo $(CONFIG_TOUCH); \
		$(QT_CONFIG) 2>$(CONFIG_LOG); \
		touch $(CONFIG_TOUCH); \
	fi

