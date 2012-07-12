#! /usr/bin/python
#coding=utf-8 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## @file    inc_glb.py
#  @brief   buildsys的全局变量， 相当于define，无需修改。
#  @author  meegoo.tsui@gmail.com
#  @date    2012/07/11
#
#  1. http://www.sthurlow.com/python/lesson06/

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## 字典。
class glb:
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ## The constructor.
    def __init__(self):
        ## build 配置文件名称
        self.build_ini = "build.ini"
        ## build.ini参数 - 项目名称
        self.project_name  = "project.name"       
        ## build.ini参数 - 项目路径
        self.project_path  = "project.path"
        ## build.ini参数 - 安装路径
        self.installe_path = "install.path"
        ## build.ini参数 - 源码路径
        self.source_path   = "source.path"
        ## build.ini参数 - 补丁路径
        self.patch_path    = "patch.path"

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## glb对象。
glb = glb()
