#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Makefile:
#+   automake
#+ author:
#+   meegoo.tsui@gmail.com
#+ date:
#+   2012/10/03
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-include buildsys.mak

# 安装包路径及文件名
TAR_PATH = $(HOME)/workspace/open/tar
TAR_FILE = $(TAR_PATH)/$(PROJECT).tar.gz
URL      = http://ftp.gnu.org/gnu/automake/$(PROJECT).tar.gz

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
all: download
	cd $(SRC_DIR)/$(PROJECT); \
	if [ ! -d $(SRC_DIR)/$(PROJECT)-build ]; then \
		mkdir -p $(SRC_DIR)/$(PROJECT)-build; \
		cd $(SRC_DIR)/$(PROJECT)-build; \
		$(SRC_DIR)/$(PROJECT)/configure --prefix=$(EXEC_DIR); \
	fi
	cd $(SRC_DIR)/$(PROJECT)-build; \
	make

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
clean: 
	if [ -d $(SRC_DIR)/$(PROJECT)-build ]; then \
		cd $(SRC_DIR)/$(PROJECT)-build; \
		make clean; \
	fi
	rm -f buildsys.mak

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
install: 
	if [ -d $(SRC_DIR)/$(PROJECT)-build ]; then \
		cd $(SRC_DIR)/$(PROJECT)-build; \
		make install; \
	fi
	@echo "生成软链接 ..."
	if [ ! -d $(HOME)/.bin ]; then \
		mkdir -p $(HOME)/.bin; \
	fi
	if [ ! -f $(HOME)/.bin/$(PROJECT) ]; then \
		ln -s $(EXEC_DIR)/bin/automake $(HOME)/.bin/$(PROJECT); \
	fi	

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
download:
	if [ ! -d $(TAR_PATH) ]; then \
		echo "生成源码包路径 ..."; \
		mkdir -p $(TAR_PATH); \
	fi
	if [ ! -f $(TAR_FILE) ]; then \
		echo "下载源码包 ..."; \
		wget $(URL) -P $(TAR_PATH); \
	fi
	if [ ! -d $(SRC_DIR) ]; then \
		echo "生成编译路径 ..."; \
		mkdir -p $(SRC_DIR); \
	fi
	if [ ! -d $(SRC_DIR)/$(PROJECT) ]; then \
		echo "解压源码包 ..."; \
		tar -zxf $(TAR_FILE) -C $(SRC_DIR); \
	fi

