#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Makefile:
#+   traceroute
#+ author:
#+   meegoo.tsui@gmail.com
#+ date:
#+   2012/07/09
#+ Lawrence Berkeley National Laboratory (LBNL)
#+ http://ee.lbl.gov/
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
include buildsys.mak

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 源码位置
TAR_PATH          = $(HOME)/workspace/open/tar
TAR_FILE          = $(TAR_PATH)/$(PROJECT).tar.gz
URL               = ftp://ftp.ee.lbl.gov/$(PROJECT).tar.gz

# 版本
VER               = 2.1a15

# 编译路径
BUILD_DIR         = $(SRC_DIR)/$(PROJECT)-$(VER)

# 配置标志文件
CONFIG_TOUCH      = config.touch
# 配置日志
CONFIG_LOG        = $(PWD)/configure.log
# 编译日志
MAKE_LOG          = $(PWD)/make.log

# 配置选项
TRACEROUTE_CONFIG = ./configure

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
all: copy config
	@set -e; \
	if [ -d $(BUILD_DIR) ]; then \
		cd $(BUILD_DIR); \
		make all 2>$(MAKE_LOG); \
	fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
clean: copy config
	@set -e; \
	if [ -d $(BUILD_DIR) ]; then \
		cd $(BUILD_DIR); \
		make clean; \
	fi
	@rm -f buildsys.mak *.log

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
install: 
	@set -e; \
	if [ -d $(BUILD_DIR) ]; then \
		cd $(BUILD_DIR); \
		sudo make install; \
	fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
copy:
	@set -e; \
	if [ ! -f $(TAR_FILE) ]; then \
		echo "下载源码包 ..."; \
		wget $(URL) -P $(TAR_PATH); \
	fi
	if [ ! -d $(SRC_DIR) ]; then \
		echo "生成编译路径 ..."; \
		mkdir -p $(SRC_DIR); \
	fi
	if [ ! -d $(BUILD_DIR) ]; then \
		echo "解压源码包 ..."; \
		tar -zxf $(TAR_FILE) -C $(SRC_DIR); \
	fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
config:
	@set -e; \
	cd $(BUILD_DIR); \
	if [ ! -f $(CONFIG_TOUCH) ]; then \
		echo $(CONFIG_TOUCH); \
		$(TRACEROUTE_CONFIG) 2>$(CONFIG_LOG); \
		touch $(CONFIG_TOUCH); \
	fi

