#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Makefile:
#+   Qt x11
#+ author:
#+   meegoo.tsui@gmail.com
#+ date:
#+   2012/07/07
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
include buildsys.mak

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Qt 源码位置
QT_GIT_PATH  = $(HOME)/git/open/qt
# Qt 配置标志文件
CONFIG_TOUCH = config.touch
# Qt 配置日志
CONFIG_LOG   = $(PWD)/configure.log
# Qt 编译日志
MAKE_LOG     = $(PWD)/make.log

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
all: copy config
	cd $(SRC_DIR);  make 2>$(MAKE_LOG)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
clean:
	@if [ -d $(SRC_DIR) ]; then \
		cd $(SRC_DIR); \
		if [ -f $(CONFIG_TOUCH) ]; then \
			make confclean; \
			rm -f $(CONFIG_TOUCH); \
		fi \
	fi
	@rm -f buildsys.mak $(CONFIG_LOG) $(MAKE_LOG)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
install: copy
	@cd $(SRC_DIR); \
	sudo make install

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
copy:
	@if [ ! -d $(SRC_DIR) ]; then \
		echo "Qt源码不存在，复制..."; \
		cp -r $(QT_GIT_PATH) $(SRC_DIR); \
	fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
config:
	@cd $(SRC_DIR); \
	if [ ! -f $(CONFIG_TOUCH) ]; then \
		echo $(CONFIG_TOUCH); \
		./configure -v -prefix /opt/qte-x11 -qvfb 2>$(CONFIG_LOG); \
		touch $(CONFIG_TOUCH); \
	fi

