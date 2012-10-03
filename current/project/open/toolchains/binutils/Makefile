#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+ Makefile:
#+   binutils
#+ author:
#+   meegoo.tsui@gmail.com
#+ date:
#+   2012/10/03
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-include buildsys.mak

# 安装包路径及文件名
TAR_PATH = $(HOME)/workspace/open/tar
TAR_FILE = $(TAR_PATH)/$(PROJECT).tar.bz2
URL      = http://ftp.gnu.org/gnu/binutils/$(PROJECT).tar.bz2

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
all: download
	cd $(SRC_DIR)/$(PROJECT); \
	if [ ! -d $(SRC_DIR)/$(PROJECT)-build ]; then \
		mkdir -p $(SRC_DIR)/$(PROJECT)-build; \
		cd $(SRC_DIR)/$(PROJECT)-build; \
		$(SRC_DIR)/$(PROJECT)/configure --prefix=$(EXEC_DIR) --enable-shared ; \
	fi
	cd $(SRC_DIR)/$(PROJECT)-build; \
	make tooldir=$(EXEC_DIR) 

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
		make tooldir=$(EXEC_DIR) install; \
	fi
	@echo "生成软链接 ..."

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
		tar -jxf $(TAR_FILE) -C $(SRC_DIR); \
	fi

