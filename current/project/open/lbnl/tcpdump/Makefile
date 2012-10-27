#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Makefile:
#+   tcpdump
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
TCPDUMP_GIT_PATH = $(HOME)/workspace/open/git/lbnl/tcpdump
MAKE_PATH        = $(PWD)

# 版本
TCPDUMP_VER      = tcpdump_4_3rel0

# 编译路径
SRC_DIR         := $(SRC_DIR)-$(TCPDUMP_VER)

# 安装路径
PREFIX           = $(EXEC_DIR)/$(TCPDUMP_VER)

# 配置标志文件
CONFIG_TOUCH     = config.touch
# 配置日志
CONFIG_LOG       = $(PWD)/configure.log
# 编译日志
MAKE_LOG         = $(PWD)/make.log

# 配置选项
TCPDUMP_CONFIG   = $(TCPDUMP_GIT_PATH)/configure

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
all: copy config
	@set -e; \
	if [ -d $(SRC_DIR) ]; then \
		cd $(SRC_DIR); \
		make 2>$(MAKE_LOG); \
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
	if [ ! -d $(TCPDUMP_GIT_PATH) ]; then \
		echo "克隆tcpdump源码..."; \
		git clone git://bpf.tcpdump.org/tcpdump $(TCPDUMP_GIT_PATH); \
	fi; \
	cd $(TCPDUMP_GIT_PATH); \
	git reset --hard; \
	git clean -fdx; \
	git checkout $(TCPDUMP_VER); \
	if [ ! -d $(SRC_DIR) ]; then \
		mkdir -p $(SRC_DIR); \
	fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
config:
	@set -e; \
	cd $(SRC_DIR); \
	if [ ! -f $(CONFIG_TOUCH) ]; then \
		echo $(CONFIG_TOUCH); \
		$(TCPDUMP_CONFIG) 2>$(CONFIG_LOG); \
		touch $(CONFIG_TOUCH); \
	fi

