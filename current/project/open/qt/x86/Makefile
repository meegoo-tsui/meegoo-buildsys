#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Makefile:
#+   Qt x86
#+ author:
#+   meegoo.tsui@gmail.com
#+ date:
#+   2012/07/07
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
include buildsys.mak
include ../qt.mak

# x86 64 配置选项
QT_CONFIG = $(QT_GIT_PATH)/configure \
                -prefix $(EXEC_DIR) \
                -embedded x86 \
                -platform  qws/linux-x86-g++ \
                -xplatform qws/linux-x86-g++ \
                -depths 16,24,32 -no-cups \
                -no-largefile -no-accessibility -no-openssl \
                -qt-mouse-pc -qt-mouse-qvfb -qt-mouse-linuxtp -qt-mouse-linuxinput -plugin-mouse-linuxtp -plugin-mouse-pc -fast \
                -plugin-gfx-qvfb
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
all: all_base

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
clean: clean_base

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
install: install_base
	@if [ ! -f $(EXEC_DIR)/bin/qvfb ]; then \
		echo "创建qvfb链接 ..."; \
		sudo ln -s $(EXEC_DIR)/../qte-x11/bin/qvfb $(EXEC_DIR)/bin/qvfb; \
	fi

