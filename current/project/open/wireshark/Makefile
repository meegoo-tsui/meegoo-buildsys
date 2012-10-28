#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Makefile:
#+   wireshark
#+ author:
#+   meegoo.tsui@gmail.com
#+ date:
#+   2012/07/11
#+ http://blog.163.com/dengwei20071015@126/blog/static/61593913200911993452446/
#+ sudo apt-get install gnome-core-devel
#+ http://packetlife.net/blog/2010/mar/19/sniffing-wireshark-non-root-user/
#+ sudo groupadd wireshark
#+ sudo usermod -a -G wireshark meegoo
#+ newgrp wireshark
#+ sudo chgrp wireshark /usr/local/bin/dumpcap 
#+ sudo chmod 750 /usr/local/bin/dumpcap 
#+ sudo sudo setcap cap_net_raw,cap_net_admin=eip /usr/local/bin/dumpcap 
#+ sudo sudo getcap /usr/local/bin/dumpcap
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
include buildsys.mak

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 源码位置
WIRESHARK_SVN    = $(HOME)/workspace/open/svn/wireshark

# 安装路径
PREFIX           = $(EXEC_DIR)

# 配置标志文件
CONFIG_TOUCH     = config.touch
# 配置日志
CONFIG_LOG       = $(PWD)/configure.log
# 编译日志
MAKE_LOG         = $(PWD)/make.log

# 配置选项
WIRESHARK_CONFIG = $(WIRESHARK_SVN)/configure

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
	if [ ! -d $(WIRESHARK_SVN) ]; then \
		echo "checkout wireshark ..."; \
		svn co http://anonsvn.wireshark.org/wireshark/trunk $(WIRESHARK_SVN); \
		cd $(WIRESHARK_SVN); \
		./autogen.sh; \
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
		$(WIRESHARK_CONFIG) 2>$(CONFIG_LOG); \
		touch $(CONFIG_TOUCH); \
	fi

