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
QT_GIT_PATH   = $(HOME)/git/open/qt
# Qt 配置标志文件
CONFIG_TOUCH  = config.touch
# Qt 配置日志
CONFIG_LOG    = $(PWD)/configure.log
# Qt 编译日志
MAKE_LOG      = $(PWD)/make.log
# x86 64 配置选项
X86_64_CONFIG = ./configure \
                -prefix $(EXEC_DIR) \
                -embedded x86_64 \
                -platform  qws/linux-x86_64-g++ \
                -xplatform qws/linux-x86_64-g++ \
                -depths 16,24,32 -no-cups \
                -no-largefile -no-accessibility -no-openssl \
                -qt-mouse-pc -qt-mouse-qvfb -qt-mouse-linuxtp -qt-mouse-linuxinput -plugin-mouse-linuxtp -plugin-mouse-pc -fast \
                -plugin-gfx-qvfb

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
	@if [ ! -d $(QT_GIT_PATH) ]; then \
		echo "克隆Qt源码..."; \
		git clone git://gitorious.org/qt/qt.git $(QT_GIT_PATH); \
	fi
	@if [ ! -d $(SRC_DIR) ]; then \
		echo "复制Qt源码..."; \
		cp -r $(QT_GIT_PATH) $(SRC_DIR); \
	fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
config:
	@cd $(SRC_DIR); \
	if [ ! -f $(CONFIG_TOUCH) ]; then \
		echo $(CONFIG_TOUCH); \
		$(X86_64_CONFIG) 2>$(CONFIG_LOG); \
		touch $(CONFIG_TOUCH); \
	fi

