#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Makefile:
#+   Qt x11
#+ author:
#+   meegoo.tsui@gmail.com
#+ date:
#+   2012/07/07
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
include buildsys.mak
include ../qt.mak

# x11 配置选项
QT_CONFIG   = $(QT_GIT_PATH)/configure -v -prefix $(EXEC_DIR) -qvfb

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
all: all_base

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
clean: clean_base

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
install: install_base
	@cd $(SRC_DIR)/tools/qvfb; \
	make; \
	sudo make install

