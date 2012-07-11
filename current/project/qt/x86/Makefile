#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Makefile:
#+   Qt x86-64
#+ author:
#+   meegoo.tsui@gmail.com
#+ date:
#+   2012/07/07
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
include buildsys.mak

# x86 64 配置选项
QT_CONFIG = ./configure \
                -prefix $(EXEC_DIR) \
                -embedded x86_64 \
                -platform  qws/linux-x86_64-g++ \
                -xplatform qws/linux-x86_64-g++ \
                -depths 16,24,32 -no-cups \
                -no-largefile -no-accessibility -no-openssl \
                -qt-mouse-pc -qt-mouse-qvfb -qt-mouse-linuxtp -qt-mouse-linuxinput -plugin-mouse-linuxtp -plugin-mouse-pc -fast \
                -plugin-gfx-qvfb

include ../qt.mak

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
all: all_base

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
clean: clean_base

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
install: install_base
	@if [ ! -f $(EXEC_DIR)/bin/qvfb ]; then \
		echo "创建qvfb链接 ..."; \
		sudo ln -s /opt/qte-x11/bin/qvfb $(EXEC_DIR)/bin/qvfb; \
	fi

